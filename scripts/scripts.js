/* ─── NAV SCROLL ─── */
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 50);
}, { passive: true });

/* ─── MOBILE DRAWER ─── */
const burger = document.getElementById('burger');
const drawer = document.getElementById('drawer');

burger.addEventListener('click', () => {
  const open = drawer.classList.toggle('open');
  burger.setAttribute('aria-expanded', open);
  document.body.style.overflow = open ? 'hidden' : '';
  burger.innerHTML = open
    ? '<span style="transform:rotate(45deg) translate(4px,5px)"></span><span style="opacity:0"></span><span style="transform:rotate(-45deg) translate(4px,-5px)"></span>'
    : '<span></span><span></span><span></span>';
});

drawer.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    drawer.classList.remove('open');
    document.body.style.overflow = '';
    burger.setAttribute('aria-expanded', false);
    burger.innerHTML = '<span></span><span></span><span></span>';
  });
});

/* ─── SCROLL REVEAL ─── */
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.08, rootMargin: '0px 0px -36px 0px' });

document.querySelectorAll('.r').forEach(el => {
  if (el.closest('.hero')) {
    el.classList.add('in');
  } else {
    io.observe(el);
  }
});

/* ─── SMOOTH SCROLL ─── */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      window.scrollTo({
        top: target.getBoundingClientRect().top + pageYOffset - 76,
        behavior: 'smooth'
      });
    }
  });
});

/* ─── INQUIRY FORM ─── */
document.getElementById('inquiry-form').addEventListener('submit', e => {
  e.preventDefault();
  const form = e.target;
  const name  = form.querySelector('#f-name').value.trim();
  const phone = form.querySelector('#f-phone').value.trim();
  const goal  = form.querySelector('#f-goal').value;
  if (!name || !phone || !goal) return;
  form.style.display = 'none';
  document.getElementById('form-ok').style.display = 'block';
});
