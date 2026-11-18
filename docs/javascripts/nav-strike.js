// Sidebar: mọi phase / backlog mặc định gạch ngang, để tập trung viết plan mới (anh chốt 2026-11-02;
// trước đó chỉ gạch Backlog + KO LÀM, chốt 2026-11-01). Không gạch trang chung (Master Plan, Quy trình build,
// Setup, Cách dùng…) và Version 12 — chỗ viết plan mới.
// Nút ↺ bỏ gạch từng mục; danh sách mục đã bỏ gạch lưu trong localStorage (riêng từng trình duyệt).
(function () {
  var KEY = 'nr-nav-unstruck-v2'; // đổi khoá → mục từng bỏ gạch theo luật cũ được gạch lại hết
  var PLAN = /^(⭐\s*)?(Phase|Backlog|Tổng quan (Version|Hoàn thiện)|Build App)\b/;
  var KEEP = /Version 12/;
  var KO_LAM = /^(⛔\s*)?KO LÀM|^Đã xong/; // cả trang phụ trong nhóm đã xong (bản đồ nguồn gap…)
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
  function add(a, unstruck) {
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
      if (!on) list.push(id);
      save(list);
      paint(li, btn, on);
    });
    paint(li, btn, unstruck.indexOf(id) === -1);
    li.classList.add('nr-strikeable');
    li.appendChild(btn);
  }
  function isPlan(a) {
    var text = a.textContent.trim();
    if (!PLAN.test(text) || KEEP.test(text)) return false;
    var sec = a.closest('li.md-nav__item--nested');
    var label = sec && sec.querySelector(':scope > label.md-nav__link');
    return !(label && KEEP.test(label.textContent));
  }
  function run() {
    var unstruck = load();
    var nav = document.querySelector('.md-nav--primary');
    if (!nav) return;
    nav.querySelectorAll('a.md-nav__link').forEach(function (a) {
      if (a.closest('.md-nav--secondary') || (a.getAttribute('href') || '#').charAt(0) === '#') return;
      var inKoLam = false;
      for (var p = a.closest('li.md-nav__item--nested'); p; p = p.parentElement.closest('li.md-nav__item--nested')) {
        var l = p.querySelector(':scope > label.md-nav__link');
        if (l && KO_LAM.test(l.textContent.trim())) inKoLam = true;
      }
      if (inKoLam || isPlan(a)) add(a, unstruck);
    });
    // nhóm con trong KO LÀM (Account, Version 5–8…): nhãn nhóm luôn gạch
    nav.querySelectorAll('li.md-nav__item--nested').forEach(function (li) {
      var label = li.querySelector(':scope > label.md-nav__link');
      var parent = li.parentElement.closest('li.md-nav__item--nested');
      var pl = parent && parent.querySelector(':scope > label.md-nav__link');
      if (label && pl && KO_LAM.test(pl.textContent.trim())) li.classList.add('nr-struck-group');
    });
  }
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(run); else document.addEventListener('DOMContentLoaded', run);
})();
