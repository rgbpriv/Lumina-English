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
const inquiryForm = document.getElementById('inquiry-form');
const formOk  = document.getElementById('form-ok');
const formErr = document.getElementById('form-err');

function showFormError(msg) {
  if (!formErr) return;
  formErr.textContent = msg;
  formErr.style.display = 'block';
}

if (inquiryForm) {
  inquiryForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const btn  = form.querySelector('.form-btn');
    const data = {
      name:    form.querySelector('#f-name').value.trim(),
      phone:   form.querySelector('#f-phone').value.trim(),
      email:   form.querySelector('#f-email').value.trim(),
      goal:    form.querySelector('#f-goal').value,
      message: form.querySelector('#f-msg').value.trim(),
      website: form.querySelector('[name="website"]').value, // honeypot
    };

    if (!data.name || !data.phone || !data.goal) {
      showFormError('Please fill in your name, phone, and goal.');
      return;
    }

    if (formErr) formErr.style.display = 'none';
    const originalLabel = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = 'Sending…';

    try {
      const res = await fetch('/api/inquiry', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      const json = await res.json().catch(() => ({}));
      if (!res.ok || !json.ok) {
        throw new Error(json.error || 'Submission failed. Please try again.');
      }
      form.style.display = 'none';
      formOk.style.display = 'block';
      formOk.scrollIntoView({ behavior: 'smooth', block: 'center' });
    } catch (err) {
      btn.disabled = false;
      btn.innerHTML = originalLabel;
      showFormError(err.message || 'Something went wrong. Please try again or call us directly.');
    }
  });
}
