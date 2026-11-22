// Menu na telefonie i linia pod przyklejonym nagłówkiem.
(function () {
  var head = document.getElementById('site-head');
  var btn = head && head.querySelector('.menu-btn');
  if (btn) {
    btn.addEventListener('click', function () {
      var open = head.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    head.querySelectorAll('nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        head.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && head.classList.contains('open')) {
        head.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.focus();
      }
    });
  }
  var bar = document.querySelector('.head-bar');
  if (bar) {
    var onScroll = function () { bar.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }
})();

// Podświetlenie w menu sekcji, którą właśnie czytasz.
(function () {
  if (!('IntersectionObserver' in window)) return;
  var links = {};
  document.querySelectorAll('#menu a[href^="#"]').forEach(function (a) { links[a.getAttribute('href').slice(1)] = a; });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      Object.keys(links).forEach(function (id) { links[id].removeAttribute('aria-current'); });
      var a = links[e.target.id]; if (a) a.setAttribute('aria-current', 'location');
    });
  }, { rootMargin: '-30% 0px -60% 0px' });
  Object.keys(links).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
})();
