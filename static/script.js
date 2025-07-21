
document.addEventListener('DOMContentLoaded', function() {
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');

  if (hamburger && navMenu) {
    hamburger.addEventListener('click', function() {
      hamburger.classList.toggle('active');
      navMenu.classList.toggle('active');
    });

    // Close menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navMenu.classList.remove('active');
    }));
  }

  // Theme toggle functionality
  const themeToggle = document.getElementById('themeToggle');
  const body = document.body;

  // Check for saved theme preference or default to dark mode
  const savedTheme = localStorage.getItem('theme') || 'dark';

  if (savedTheme === 'light') {
    body.classList.add('light-theme');
    if (themeToggle) themeToggle.textContent = '☀️';
  } else {
    if (themeToggle) themeToggle.textContent = '🌙';
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      body.classList.toggle('light-theme');

      if (body.classList.contains('light-theme')) {
        themeToggle.textContent = '☀️';
        localStorage.setItem('theme', 'light');
      } else {
        themeToggle.textContent = '🌙';
        localStorage.setItem('theme', 'dark');
      }
    });
  }

  // Form handling for email signups
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const email = this.querySelector('input[type="email"]');
      if (email && email.value) {
        alert('Thank you for signing up! We\'ll be in touch soon.');
        email.value = '';
      }
    });
  });
});
