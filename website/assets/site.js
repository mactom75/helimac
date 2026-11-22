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

// Logo w nagłówku pojawia się dopiero, gdy duże logo z części otwierającej zniknie z ekranu.
(function () {
  var big = document.querySelector('.hero-logo');
  var bar = document.querySelector('.head-bar');
  if (!big || !bar || !('IntersectionObserver' in window)) return;
  bar.classList.add('brand-auto');
  new IntersectionObserver(function (e) {
    bar.classList.toggle('show-brand', !e[0].isIntersecting);
  }, { rootMargin: '-70px 0px 0px 0px' }).observe(big);
})();

// Lista darczyńców z pliku /supporters.json (uzupełnianego na bieżąco).
(function () {
  var list = document.querySelector('.donor-list');
  if (!list || !window.fetch) return;
  var countEl = document.querySelector('.donors-count');
  var lang = document.documentElement.lang || 'pl';
  function label(n) {
    if (!countEl) return '';
    if (lang === 'pl') {
      var m10 = n % 10, m100 = n % 100;
      if (n === 1) return countEl.dataset.one;
      if (m10 >= 2 && m10 <= 4 && (m100 < 12 || m100 > 14)) return countEl.dataset.few;
      return countEl.dataset.countLabel;
    }
    return n === 1 ? countEl.dataset.one : countEl.dataset.countLabel;
  }
  fetch('/supporters.json', { cache: 'no-cache' })
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var people = (data && data.supporters) || [];
      list.textContent = '';
      if (!people.length) {
        var li = document.createElement('li'); li.className = 'empty';
        li.textContent = list.dataset.empty; list.appendChild(li); return;
      }
      people.forEach(function (p) {
        var li = document.createElement('li');
        var name = document.createElement('span'); name.className = 'donor-name';
        name.textContent = (p.name && String(p.name).trim()) || list.dataset.anon;
        li.appendChild(name);
        if (p.date) {
          var t = document.createElement('time'); t.dateTime = p.date;
          var d = p.date.split('-'); t.textContent = d.length === 3 ? d[2] + '.' + d[1] + '.' + d[0] : p.date;
          li.appendChild(t);
        }
        list.appendChild(li);
      });
      if (countEl) {
        var b = document.createElement('strong'); b.textContent = people.length + ' ';
        countEl.textContent = ''; countEl.appendChild(b); countEl.appendChild(document.createTextNode(label(people.length)));
      }
    })
    .catch(function () {});
})();
