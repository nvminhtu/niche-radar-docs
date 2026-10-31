// Sidebar: nút gạch ngang cho từng plan trong "Backlog · làm sau" và "KO LÀM", đỡ phân tâm. Lưu trong localStorage (riêng từng trình duyệt).
(function () {
  var KEY = 'nr-nav-strike';
  var SECTION = /^(⛔\s*)?KO LÀM|^Backlog ·/;
  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { return []; }
  }
  function save(list) {
    try { localStorage.setItem(KEY, JSON.stringify(list)); } catch (e) { /* trình duyệt chặn lưu → chỉ gạch tới khi đổi trang */ }
  }
  function slug(a) {
    return a.pathname.split('/').filter(Boolean).slice(-2).join('/');
  }
  function paint(li, btn, on) {
    li.classList.toggle('nr-struck', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.title = on ? 'Bỏ gạch ngang' : 'Gạch ngang';
    btn.textContent = on ? '↺' : '—';
  }
  function add(a, struck) {
    var li = a.closest('li.md-nav__item');
    if (!li || li.querySelector(':scope > .nr-strike')) return;
    var id = slug(a);
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'nr-strike';
    btn.setAttribute('aria-label', a.textContent.trim());
    btn.addEventListener('click', function () {
      var list = load().filter(function (x) { return x !== id; });
      var on = !li.classList.contains('nr-struck');
      if (on) list.push(id);
      save(list);
      paint(li, btn, on);
    });
    paint(li, btn, struck.indexOf(id) !== -1);
    li.classList.add('nr-strikeable');
    li.appendChild(btn);
  }
  function run() {
    var struck = load();
    document.querySelectorAll('.md-nav--primary li.md-nav__item--nested > label.md-nav__link').forEach(function (label) {
      if (!SECTION.test(label.textContent.trim())) return;
      label.parentNode.querySelectorAll('a.md-nav__link').forEach(function (a) {
        if (!a.closest('.md-nav--secondary') && a.getAttribute('href').charAt(0) !== '#') add(a, struck);
      });
    });
  }
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(run); else document.addEventListener('DOMContentLoaded', run);
})();
