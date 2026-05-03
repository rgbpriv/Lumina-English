/**
 * Lumina inquiry server
 * ─────────────────────
 * • Serves the static site (index.html, styles/, scripts/)
 * • POST /api/inquiry  → appends a row to data/inquiries.csv
 * • GET  /api/inquiries.csv → downloads the CSV (basic admin guard via ?key=)
 *
 * No npm dependencies — uses only Node's built-in http/fs/path/url.
 *
 * Run:
 *   node server/server.js
 *   PORT=4000 ADMIN_KEY=secret node server/server.js
 */

const http = require('http');
const fs   = require('fs');
const path = require('path');
const url  = require('url');

const PORT      = parseInt(process.env.PORT || '3000', 10);
const ADMIN_KEY = process.env.ADMIN_KEY || 'change-me';
const ROOT      = path.resolve(__dirname, '..');
const DATA_DIR  = path.join(ROOT, 'data');
const CSV_PATH  = path.join(DATA_DIR, 'inquiries.csv');

const CSV_HEADERS = [
  'timestamp_iso',
  'name',
  'phone',
  'email',
  'goal',
  'message',
  'ip',
  'user_agent',
];

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css':  'text/css; charset=utf-8',
  '.js':   'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg':  'image/svg+xml',
  '.png':  'image/png',
  '.jpg':  'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.ico':  'image/x-icon',
  '.woff': 'font/woff',
  '.woff2':'font/woff2',
  '.txt':  'text/plain; charset=utf-8',
};

/* ─── CSV helpers ─── */
function csvEscape(value) {
  if (value === null || value === undefined) return '';
  const s = String(value);
  // Strip control chars except tab/newline; protect against CSV/Excel formula injection.
  const cleaned = s.replace(/[\x00-\x08\x0B\x0C\x0E-\x1F]/g, '');
  const safe = /^[=+\-@\t\r]/.test(cleaned) ? "'" + cleaned : cleaned;
  if (/[",\r\n]/.test(safe)) return '"' + safe.replace(/"/g, '""') + '"';
  return safe;
}

function ensureCsv() {
  if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });
  if (!fs.existsSync(CSV_PATH)) {
    fs.writeFileSync(CSV_PATH, CSV_HEADERS.join(',') + '\n', 'utf8');
  }
}

function appendRow(row) {
  ensureCsv();
  const line = CSV_HEADERS.map((h) => csvEscape(row[h])).join(',') + '\n';
  fs.appendFileSync(CSV_PATH, line, 'utf8');
}

/* ─── validation ─── */
function validate(body) {
  const errors = [];
  const name  = (body.name  || '').trim();
  const phone = (body.phone || '').trim();
  const email = (body.email || '').trim();
  const goal  = (body.goal  || '').trim();
  const message = (body.message || '').trim();

  if (name.length < 2 || name.length > 120) errors.push('name must be 2–120 chars');
  if (phone.length < 6 || phone.length > 40) errors.push('phone must be 6–40 chars');
  if (email && (email.length > 200 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)))
    errors.push('email is invalid');
  if (!goal || goal.length > 60) errors.push('goal is required');
  if (message.length > 2000) errors.push('message too long');

  return { errors, clean: { name, phone, email, goal, message } };
}

/* ─── HTTP helpers ─── */
function readBody(req, limit = 32 * 1024) {
  return new Promise((resolve, reject) => {
    let size = 0;
    const chunks = [];
    req.on('data', (c) => {
      size += c.length;
      if (size > limit) {
        reject(Object.assign(new Error('payload too large'), { status: 413 }));
        req.destroy();
        return;
      }
      chunks.push(c);
    });
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

function sendJson(res, status, body) {
  res.writeHead(status, {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'no-store',
  });
  res.end(JSON.stringify(body));
}

function sendStatic(req, res, pathname) {
  let rel = decodeURIComponent(pathname);
  if (rel === '/' || rel === '') rel = '/index.html';

  // prevent path traversal
  const filePath = path.normalize(path.join(ROOT, rel));
  if (!filePath.startsWith(ROOT)) {
    res.writeHead(403); res.end('Forbidden'); return;
  }
  // never serve server source or data dir
  if (filePath.startsWith(path.join(ROOT, 'server')) ||
      filePath.startsWith(DATA_DIR) ||
      filePath.startsWith(path.join(ROOT, 'node_modules'))) {
    res.writeHead(404); res.end('Not Found'); return;
  }

  fs.stat(filePath, (err, stat) => {
    if (err || !stat.isFile()) { res.writeHead(404); res.end('Not Found'); return; }
    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, {
      'Content-Type': MIME[ext] || 'application/octet-stream',
      'Cache-Control': 'public, max-age=300',
    });
    fs.createReadStream(filePath).pipe(res);
  });
}

/* ─── Rate limiting (in-memory, per-IP) ─── */
const RL_WINDOW_MS = 60 * 1000;
const RL_MAX_HITS  = 6;
const rl = new Map();
function rateLimited(ip) {
  const now = Date.now();
  const entry = rl.get(ip) || [];
  const recent = entry.filter((t) => now - t < RL_WINDOW_MS);
  recent.push(now);
  rl.set(ip, recent);
  return recent.length > RL_MAX_HITS;
}
setInterval(() => {
  const cutoff = Date.now() - RL_WINDOW_MS;
  for (const [ip, hits] of rl) {
    const fresh = hits.filter((t) => t > cutoff);
    if (fresh.length) rl.set(ip, fresh); else rl.delete(ip);
  }
}, 5 * 60 * 1000).unref();

/* ─── routes ─── */
async function handleInquiry(req, res, ip) {
  if (rateLimited(ip)) return sendJson(res, 429, { ok: false, error: 'too many requests' });

  let raw;
  try { raw = await readBody(req); }
  catch (e) { return sendJson(res, e.status || 400, { ok: false, error: 'bad request' }); }

  let body;
  try { body = raw ? JSON.parse(raw) : {}; }
  catch { return sendJson(res, 400, { ok: false, error: 'invalid json' }); }

  // honeypot
  if (body.website && String(body.website).trim() !== '') {
    return sendJson(res, 200, { ok: true });
  }

  const { errors, clean } = validate(body);
  if (errors.length) return sendJson(res, 422, { ok: false, error: errors.join('; ') });

  try {
    appendRow({
      timestamp_iso: new Date().toISOString(),
      name:    clean.name,
      phone:   clean.phone,
      email:   clean.email,
      goal:    clean.goal,
      message: clean.message,
      ip,
      user_agent: (req.headers['user-agent'] || '').slice(0, 240),
    });
  } catch (e) {
    console.error('CSV write failed:', e);
    return sendJson(res, 500, { ok: false, error: 'could not save inquiry' });
  }

  console.log(`[inquiry] ${clean.name} · ${clean.goal} · ${ip}`);
  sendJson(res, 200, { ok: true });
}

function handleCsvDownload(req, res, parsed) {
  const key = parsed.query.key;
  if (!key || key !== ADMIN_KEY) {
    res.writeHead(401); res.end('unauthorized'); return;
  }
  ensureCsv();
  res.writeHead(200, {
    'Content-Type': 'text/csv; charset=utf-8',
    'Content-Disposition': 'attachment; filename="lumina-inquiries.csv"',
    'Cache-Control': 'no-store',
  });
  fs.createReadStream(CSV_PATH).pipe(res);
}

/* ─── server ─── */
const server = http.createServer(async (req, res) => {
  const parsed = url.parse(req.url, true);
  const ip = (req.headers['x-forwarded-for'] || req.socket.remoteAddress || '')
    .toString().split(',')[0].trim();

  // CORS (allow same-origin + simple cross-origin POSTs in dev)
  res.setHeader('Access-Control-Allow-Origin', req.headers.origin || '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') { res.writeHead(204); res.end(); return; }

  if (req.method === 'POST' && parsed.pathname === '/api/inquiry') {
    return handleInquiry(req, res, ip);
  }
  if (req.method === 'GET' && parsed.pathname === '/api/inquiries.csv') {
    return handleCsvDownload(req, res, parsed);
  }
  if (req.method === 'GET') {
    return sendStatic(req, res, parsed.pathname);
  }
  res.writeHead(405); res.end('Method Not Allowed');
});

server.listen(PORT, () => {
  ensureCsv();
  console.log(`Lumina server → http://localhost:${PORT}`);
  console.log(`CSV → ${CSV_PATH}`);
  console.log(`Admin download → http://localhost:${PORT}/api/inquiries.csv?key=${ADMIN_KEY}`);
});
