// Only fetch and play project videos while they're actually visible on
// screen, so a page with several clips doesn't stream all of them at once.
document.addEventListener('DOMContentLoaded', function () {
  var videos = document.querySelectorAll('video.lazy-video');

  if (!('IntersectionObserver' in window)) {
    videos.forEach(function (video) { video.play(); });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      var video = entry.target;
      if (entry.isIntersecting) {
        video.play().catch(function () {});
      } else {
        video.pause();
      }
    });
  }, { threshold: 0.25 });

  videos.forEach(function (video) { observer.observe(video); });
});
