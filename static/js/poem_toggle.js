// Toggle between Spanish (ES) and English (EN) versions of a poem.
// Works when the detail template provides elements with these IDs:
//  - btn-es, btn-en, poem-es, (optional) poem-en

(function () {
  function initPoemToggle() {
    var esBlock = document.getElementById("poem-es");
    var enBlock = document.getElementById("poem-en");   // may not exist
    var btnES   = document.getElementById("btn-es");
    var btnEN   = document.getElementById("btn-en");

    // If there's no EN block or no buttons, nothing to do.
    if (!esBlock || !btnES || !btnEN || !enBlock) return;

    var key = "ep-poem-lang:" + window.location.pathname;

    // Helpers
    function setBtnActive(btnOn, btnOff) {
      btnOn.classList.add("btn-secondary");
      btnOn.classList.remove("btn-outline-secondary");
      btnOn.setAttribute("aria-pressed", "true");

      btnOff.classList.remove("btn-secondary");
      btnOff.classList.add("btn-outline-secondary");
      btnOff.setAttribute("aria-pressed", "false");
    }

    function showES() {
      esBlock.style.display = "";
      enBlock.style.display = "none";
      setBtnActive(btnES, btnEN);
      try { localStorage.setItem(key, "es"); } catch(e) {}
    }

    function showEN() {
      esBlock.style.display = "none";
      enBlock.style.display = "";
      setBtnActive(btnEN, btnES);
      try { localStorage.setItem(key, "en"); } catch(e) {}
    }

    // Default or remembered state
    var saved = null;
    try { saved = localStorage.getItem(key); } catch(e) {}
    if (saved === "en") { showEN(); } else { showES(); }

    // Bind clicks
    btnES.addEventListener("click", showES);
    btnEN.addEventListener("click", showEN);
  }

  // Run after DOM is ready (safe if put in <head> with defer)
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initPoemToggle);
  } else {
    initPoemToggle();
  }
})();
