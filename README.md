# Lumina English Institute

Premium single-page website for **Lumina English Institute**, Dhaka — with a zero-dependency Node.js inquiry backend that appends leads to a local CSV file.

---

## Stack

| Layer | Tech |
|---|---|
| Frontend | Vanilla HTML · CSS (custom properties) · Vanilla JS |
| Fonts | Cormorant Garamond · Inter (Google Fonts) |
| Backend | Node.js built-in `http` / `fs` — no npm dependencies |
| Data | `data/inquiries.csv` — append-only, auto-created |

---

## Project structure

```
├── index.html          # Single-page site markup
├── styles/
│   └── styles.css      # Full design system & layout
├── scripts/
│   └── scripts.js      # Nav, scroll reveal, form submission
├── server/
│   └── server.js       # Static file server + inquiry API
├── data/
│   └── inquiries.csv   # Auto-created on first form submission
├── package.json
└── .claude/
    └── launch.json     # Preview server config
```

---

## Running locally

**Requires Node.js 18+. No `npm install` needed.**

```bash
npm start
# → http://localhost:3000
```

The server serves the static site **and** handles the inquiry form API on the same port.

### Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `PORT` | `3000` | Port to listen on |
| `ADMIN_KEY` | `change-me` | Key required to download the CSV |

```bash
PORT=4000 ADMIN_KEY=mysecret npm start
```

---

## Inquiry API

### `POST /api/inquiry`

Submits a new inquiry. Validates, appends a row to `data/inquiries.csv`, and returns JSON.

**Request body (JSON)**

```json
{
  "name":    "Full Name",
  "phone":   "+8801711000000",
  "email":   "optional@email.com",
  "goal":    "ielts",
  "message": "Optional free-text note"
}
```

**Responses**

| Status | Meaning |
|---|---|
| `200 { ok: true }` | Saved successfully |
| `422 { ok: false, error: "..." }` | Validation failed |
| `429 { ok: false, error: "too many requests" }` | Rate limited (6 req/min per IP) |

### `GET /api/inquiries.csv?key=<ADMIN_KEY>`

Downloads the full CSV. Returns `401` if the key is wrong or missing.

```bash
curl "http://localhost:3000/api/inquiries.csv?key=mysecret" -o leads.csv
```

### CSV columns

```
timestamp_iso, name, phone, email, goal, message, ip, user_agent
```

---

## Security notes

- **Formula injection guard** — fields starting with `= + - @ \t \r` are prefixed with `'` before writing to CSV (Excel / Sheets safe)
- **Honeypot field** — a hidden `website` input silently discards bot submissions
- **Rate limiting** — 6 submissions per IP per 60-second window (in-memory)
- **Body cap** — requests larger than 32 KB are rejected with `413`
- **Path traversal guard** — `server/` and `data/` are never served as static files

---

## Sections

| # | Section | Description |
|---|---|---|
| 1 | Hero | Full-viewport with animated ghost letter and scroll cue |
| 2 | Marquee | Scrolling ticker of course offerings |
| 3 | Why Lumina | Traditional vs Lumina comparison table |
| 4 | How We Teach | Six teaching methods on dark background |
| 5 | The Course | One-month repeatable programme detail |
| 6 | IELTS | Band-targeted preparation approach |
| 7 | Study Abroad | Life beyond the test score |
| 8 | The Journey | Six-stage learning path |
| 9 | Outcomes | Six measurable student outcomes |
| 10 | Philosophy | Teaching principles — sticky sidebar layout |
| 11 | Stories | Editorial testimonials — Raya Morshed, Rafiqul Alom Shoeb |
| 12 | Enroll | Inquiry form wired to backend |

---

## Deployment

The site is a static folder plus a single Node process — it deploys anywhere Node runs.

**Render / Railway / Fly.io**

Set `PORT` and `ADMIN_KEY` as environment variables and point the start command to:

```bash
node server/server.js
```

**Persisting the CSV**

`data/inquiries.csv` is written to disk relative to the project root. On ephemeral platforms (Render free tier, etc.) mount a persistent volume at `/data` or export leads regularly via the admin endpoint.

---

## License

Private — all rights reserved. © 2025 Lumina English Institute, Dhaka.
