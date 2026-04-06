function openModal() {
  const modal = document.getElementById('enrollModal');
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  const modal = document.getElementById('enrollModal');
  modal.style.display = 'none';
  document.body.style.overflow = 'auto';
}

window.onclick = function (event) {
  const modal = document.getElementById('enrollModal');
  if (event.target === modal) {
    closeModal();
  }
};
