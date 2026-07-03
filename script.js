/* Ari's Mobile Detailing — interactions */
(function () {
  "use strict";

  /* ---- current year ---- */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---- header shrink on scroll ---- */
  var header = document.querySelector(".header");
  var onScroll = function () {
    if (window.scrollY > 24) header.classList.add("shrink");
    else header.classList.remove("shrink");
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---- mobile drawer ---- */
  var burger = document.getElementById("burger");
  var drawer = document.getElementById("drawer");
  var toggleDrawer = function (open) {
    var isOpen = open === undefined ? !drawer.classList.contains("open") : open;
    drawer.classList.toggle("open", isOpen);
    drawer.setAttribute("aria-hidden", String(!isOpen));
    burger.setAttribute("aria-expanded", String(isOpen));
    document.body.style.overflow = isOpen ? "hidden" : "";
  };
  if (burger) burger.addEventListener("click", function () { toggleDrawer(); });
  if (drawer) {
    drawer.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { toggleDrawer(false); });
    });
  }
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") toggleDrawer(false);
  });

  /* ---- scroll reveal ---- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- before / after slider ---- */
  var ba = document.getElementById("ba");
  if (ba) {
    var before = document.getElementById("baBefore");
    var handle = document.getElementById("baHandle");
    var range = document.getElementById("baRange");
    var afterImg = document.getElementById("baAfter");
    var beforeImg = document.getElementById("baBeforeImg");

    // clip-path keeps both full-size images pixel-aligned; only the reveal moves
    var setPos = function (pct) {
      pct = Math.max(0, Math.min(100, pct));
      before.style.clipPath = "inset(0 " + (100 - pct) + "% 0 0)";
      handle.style.left = pct + "%";
      if (range.value != pct) range.value = pct;
    };

    range.addEventListener("input", function () { setPos(parseFloat(range.value)); });

    var dragging = false;
    var posFromEvent = function (clientX) {
      var rect = ba.getBoundingClientRect();
      setPos(((clientX - rect.left) / rect.width) * 100);
    };
    var start = function (e) {
      // let the range slider handle its own keyboard/focus; drag from anywhere on image
      dragging = true;
      ba.classList.add("dragging");
      posFromEvent(e.touches ? e.touches[0].clientX : e.clientX);
    };
    var move = function (e) {
      if (!dragging) return;
      posFromEvent(e.touches ? e.touches[0].clientX : e.clientX);
    };
    var end = function () { dragging = false; ba.classList.remove("dragging"); };

    ba.addEventListener("mousedown", start);
    window.addEventListener("mousemove", move);
    window.addEventListener("mouseup", end);
    ba.addEventListener("touchstart", start, { passive: true });
    window.addEventListener("touchmove", move, { passive: true });
    window.addEventListener("touchend", end);

    setPos(50);

    /* ---- tabs: switch which pair is shown ---- */
    var tabs = document.querySelectorAll("#baTabs .ba-tab");
    var countEl = document.querySelector(".ba-count");
    if (countEl) countEl.textContent = String(tabs.length);
    var swapTo = function (tab) {
      var b = tab.getAttribute("data-before");
      var a = tab.getAttribute("data-after");
      // preload the new pair, then swap together to avoid a flash of mismatch
      var imgA = new Image();
      imgA.onload = function () {
        beforeImg.src = b;
        afterImg.src = a;
        setPos(50);
      };
      imgA.src = a;
      beforeImg.src = b; // before can load immediately under the clip
      tabs.forEach(function (t) {
        var on = t === tab;
        t.classList.toggle("is-active", on);
        t.setAttribute("aria-selected", String(on));
      });
    };
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () { swapTo(tab); });
    });
  }

  /* ---- quote form: email Ari (Web3Forms) + pre-filled text fallback ---- */
  // Get a FREE access key at https://web3forms.com (enter Ari's email — submissions
  // are emailed there). Paste it below to turn on email delivery. Until then, the
  // form falls back to opening a pre-filled text to Ari, so it always works.
  var WEB3FORMS_KEY = "42037dba-b8e4-4e8d-abe0-eee59211e5ff";

  /* ---- cursor spotlight glow on cards ---- */
  var glowCards = document.querySelectorAll(".spotlight");
  if (glowCards.length && window.matchMedia("(pointer:fine)").matches) {
    document.documentElement.classList.add("has-spotlight");
    glowCards.forEach(function (card) {
      var raf = null, mx = 0, my = 0;
      card.addEventListener("pointermove", function (e) {
        var rect = card.getBoundingClientRect();
        mx = e.clientX - rect.left;
        my = e.clientY - rect.top;
        if (raf) return;
        raf = requestAnimationFrame(function () {
          raf = null;
          card.style.setProperty("--mx", mx.toFixed(1));
          card.style.setProperty("--my", my.toFixed(1));
        });
      }, { passive: true });
    });
  }

  var form = document.getElementById("qform");
  if (form) {
    var val = function (id) {
      var el = document.getElementById(id);
      return el ? el.value.trim() : "";
    };
    var fields = function () {
      return {
        name: val("f-name"), phone: val("f-phone"), vehicle: val("f-vehicle"),
        service: val("f-service"), notes: val("f-notes")
      };
    };
    var openText = function (f) {
      var lines = ["Hi Ari, I'd like a detailing quote."];
      if (f.name) lines.push("Name: " + f.name);
      if (f.phone) lines.push("Phone: " + f.phone);
      if (f.vehicle) lines.push("Vehicle: " + f.vehicle);
      if (f.service) lines.push("Service: " + f.service);
      if (f.notes) lines.push("Details: " + f.notes);
      var body = encodeURIComponent(lines.join("\n"));
      var ua = navigator.userAgent || "";
      var sep = /iPhone|iPad|Macintosh/i.test(ua) ? "&" : "?";
      window.location.href = "sms:+14025159157" + sep + "body=" + body;
    };
    var showDone = function () {
      var done = document.getElementById("qformDone");
      if (done) { form.hidden = true; done.hidden = false; done.scrollIntoView({ block: "center" }); }
    };

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      // honeypot — bots fill this hidden field
      if (form.botcheck && form.botcheck.checked) return;
      var f = fields();

      // No key yet → just open a pre-filled text (works immediately).
      if (!WEB3FORMS_KEY || WEB3FORMS_KEY.indexOf("YOUR_") === 0) {
        openText(f);
        return;
      }

      var btn = form.querySelector('button[type="submit"]');
      var orig = btn ? btn.innerHTML : "";
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }

      fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify({
          access_key: WEB3FORMS_KEY,
          subject: "New quote request" + (f.name ? " — " + f.name : ""),
          from_name: "Ari's Mobile Detailing website",
          name: f.name, phone: f.phone, vehicle: f.vehicle,
          service: f.service, message: f.notes
        })
      })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          if (data && data.success) { showDone(); }
          else { openText(f); } // delivery failed → fall back to text
        })
        .catch(function () { openText(f); })
        .finally(function () { if (btn) { btn.disabled = false; btn.innerHTML = orig; } });
    });
  }
})();
