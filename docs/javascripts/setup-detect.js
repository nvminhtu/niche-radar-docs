// Trang Setup máy (Phase 24, lớp 1): đoán OS + chip từ trình duyệt, chỉ hiện bộ bước của máy đó. Đoán không chắc → hiện cả hai.
(function () {
  function run() {
    var p = document.getElementById('setup-detect');
    if (!p) return;
    var ua = navigator.userAgent || '';
    var plat = (navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || '';
    var os = /mac/i.test(plat) || /Mac OS X/.test(ua) ? 'mac' : /win/i.test(plat) || /Windows/.test(ua) ? 'win' : null;
    var show = function (chip) {
      var label = os === 'mac' ? 'macOS' + (chip ? ' · chip ' + chip : '') : os === 'win' ? 'Windows' : null;
      p.textContent = label ? 'Máy của bạn: ' + label + ' — chỉ hiện bước cho máy này.' : 'Chưa đoán được máy — hiện bước cho cả macOS và Windows.';
      document.querySelectorAll('.setup-os').forEach(function (el) { el.hidden = !!os && el.getAttribute('data-os') !== os; });
    };
    if (os === 'mac' && navigator.userAgentData && navigator.userAgentData.getHighEntropyValues) {
      navigator.userAgentData.getHighEntropyValues(['architecture']).then(function (v) { show(v.architecture === 'arm' ? 'Apple' : v.architecture === 'x86' ? 'Intel' : null); }, function () { show(null); });
    } else show(null);
  }
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(run); else document.addEventListener('DOMContentLoaded', run);
})();
