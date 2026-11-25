// Project pages: swap the sidebar bio for a table of contents built from
// the page's own section headers (.section-header boxes and ## headings).
// The bio stays in the HTML, so without JavaScript the sidebar looks the
// same as on every other page. Loaded only on project pages (main.html).
document.addEventListener('DOMContentLoaded', function () {
  var toc = document.querySelector('.page-toc');
  var list = toc && toc.querySelector('.page-toc__list');
  var content = document.querySelector('.content-box');
  if (!list || !content) return;

  var headers = content.querySelectorAll('.section-header, h2');
  var used = {};
  var items = [];

  function slugify(text) {
    var base = text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'section';
    var slug = base;
    for (var n = 2; used[slug] || document.getElementById(slug); n++) slug = base + '-' + n;
    used[slug] = true;
    return slug;
  }

  headers.forEach(function (el, i) {
    var label;
    if (i === 0 && el.classList.contains('section-header')) {
      // The first box is the "Course. Completed Month Year" line.
      label = 'Overview';
    } else {
      // "Project role: **Technical Lead**. I made sure..." -> "Technical Lead"
      var strong = el.classList.contains('section-header') && el.querySelector('strong');
      label = (strong ? strong.textContent : el.textContent).trim().replace(/[.:]$/, '');
    }
    if (!el.id) el.id = slugify(label);

    var link = document.createElement('a');
    link.href = '#' + el.id;
    link.textContent = label;
    var li = document.createElement('li');
    li.appendChild(link);
    list.appendChild(li);
    items.push({ target: el, link: link });
  });

  // A one-entry list isn't worth losing the bio for.
  if (items.length < 2) return;

  var bio = document.querySelector('.about-bio');
  if (bio) bio.hidden = true;
  toc.hidden = false;

  // Highlight the section currently being read: the last header that has
  // scrolled past the top third of the screen.
  if (!('IntersectionObserver' in window)) return;
  function update() {
    var line = window.innerHeight / 3;
    var current = items[0];
    items.forEach(function (item) {
      if (item.target.getBoundingClientRect().top <= line) current = item;
    });
    items.forEach(function (item) {
      if (item === current) item.link.setAttribute('aria-current', 'true');
      else item.link.removeAttribute('aria-current');
    });
  }
  var observer = new IntersectionObserver(update, {
    rootMargin: '0px 0px -66% 0px'
  });
  items.forEach(function (item) { observer.observe(item.target); });
  update();
});
