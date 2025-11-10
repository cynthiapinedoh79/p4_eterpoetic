/* jshint esversion: 11, moz: true, browser: true */

(function () {
  // Keep only the first .quote-banner on the page
  const all = Array.from(document.querySelectorAll('.quote-banner'));
  if (!all.length) return;
  all.slice(1).forEach(b => b.remove());

  // Initialize the one remaining banner
  const banners = document.querySelectorAll('.quote-banner'); // now length = 1
  banners.forEach((banner) => {
    const track   = banner.querySelector('.qb-track');
    const slides  = Array.from(track?.children || []);
    const prevBtn = banner.querySelector('.qb-prev');
    const nextBtn = banner.querySelector('.qb-next');
    if (!track || slides.length === 0) return;

    let index = Math.floor(Math.random() * slides.length);
    let timer = null;

    const go   = i => { index = (i + slides.length) % slides.length; track.style.transform = `translateX(-${index * 100}%)`; };
    const next = () => go(index + 1);
    const prev = () => go(index - 1);

    if (slides.length < 2) { prevBtn?.remove(); nextBtn?.remove(); }
    else { nextBtn?.addEventListener('click', next); prevBtn?.addEventListener('click', prev); }

    const start = () => { stop(); timer = setInterval(next, 4500); };
    const stop  = () => { if (timer) { clearInterval(timer); timer = null; } };

    banner.addEventListener('mouseenter', stop);
    banner.addEventListener('mouseleave', start);
    banner.addEventListener('focusin', stop);
    banner.addEventListener('focusout', start);
    document.addEventListener('visibilitychange', () => document.hidden ? stop() : start());

    // swipe
    let sx=0, dx=0, swiping=false;
    banner.addEventListener('touchstart', e => { swiping=true; sx=e.touches[0].clientX; dx=0; stop(); }, {passive:true});
    banner.addEventListener('touchmove',  e => { if(!swiping) return; dx=e.touches[0].clientX - sx; }, {passive:true});
    banner.addEventListener('touchend',   () => { if(!swiping) return; swiping=false; const T=Math.min(60, banner.clientWidth*0.12); if(dx<-T) next(); else if(dx>T) prev(); start(); });

    go(index);
    start();
  });
})();

