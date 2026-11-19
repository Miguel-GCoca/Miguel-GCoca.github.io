// Time on page for GoatCounter.
//
// GoatCounter has no built-in "time on page" number, so this script measures
// it and reports it as a GoatCounter *event* (the same mechanism as the
// outbound:/download: click tracking in _includes/head.html). When the
// visitor leaves, it sends one event whose path names the page plus a time
// bucket, for example:
//
//   time:/projects/cpp-robotics-capstone/ 1-2m
//
// In the dashboard, type "time:" (or "time:/projects/<slug>/") into the
// path filter to see how many views of each page landed in each bucket.
//
// Only time the page is actually visible counts: a tab opened in the
// background starts counting when the visitor switches to it, and time spent
// in another tab or app is excluded. One event per page view, sent the first
// time the page is hidden (tab switch, navigating away, closing the tab,
// switching apps on a phone). If the visitor comes back to the same tab
// afterwards, that extra time isn't added (sending again would count the
// view twice).
//
// Loaded from _includes/head.html, only when goatcounter-code is set in
// _config.yml. count.js itself refuses to send from localhost and from
// browsers opted out via #toggle-goatcounter, and that applies here too.
(function () {
	'use strict';

	// [upper bound in seconds, label]. Anything longer is "10m+".
	var BUCKETS = [
		[10, '0-10s'],
		[30, '10-30s'],
		[60, '30s-1m'],
		[120, '1-2m'],
		[300, '2-5m'],
		[600, '5-10m']
	];

	var visibleMs = 0;       // visible time banked from finished stretches
	var visibleSince = null; // start of the current visible stretch, if any
	var sent = false;

	function start() {
		if (visibleSince === null) visibleSince = Date.now();
	}

	function stop() {
		if (visibleSince === null) return;
		visibleMs += Date.now() - visibleSince;
		visibleSince = null;
	}

	function bucket(seconds) {
		for (var i = 0; i < BUCKETS.length; i++) {
			if (seconds < BUCKETS[i][0]) return BUCKETS[i][1];
		}
		return '10m+';
	}

	function report() {
		stop();
		// visibleMs is 0 for a background tab closed without ever being looked
		// at. goatcounter can be missing if count.js hasn't loaded yet (it's
		// async) or was blocked by an ad blocker.
		if (sent || visibleMs === 0) return;
		if (!window.goatcounter || !window.goatcounter.count) return;
		sent = true;
		var label = bucket(visibleMs / 1000);
		window.goatcounter.count({
			path: 'time:' + location.pathname + ' ' + label,
			title: label + ' on ' + document.title,
			event: true
		});
	}

	if (!('visibilityState' in document) || document.visibilityState === 'visible') start();

	document.addEventListener('visibilitychange', function () {
		if (document.visibilityState === 'visible') start();
		else report();
	});
	// Backup for browsers that don't fire visibilitychange on navigation.
	window.addEventListener('pagehide', report);
})();
