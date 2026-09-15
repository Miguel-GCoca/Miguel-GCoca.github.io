# Miguel Grisales Coca — Portfolio Site

Personal portfolio for Miguel Grisales Coca, hosted on GitHub Pages at
`https://miguel-gcoca.github.io/`. Repo: `Miguel-GCoca/Miguel-GCoca.github.io`
(user-site repo, so Pages serves straight from `main`, no gh-pages branch needed).

Miguel is a Mechanical Engineering student at UCF (robotics/physical AI focus).
He's actively learning Jekyll/git/web dev through this project — when making
changes, prefer explaining the mechanism (which file, why) over just doing it
silently, and keep edits scoped to what was asked.

## Design taste

For any frontend/design work in this repo — layout, CSS, typography, color,
dark-mode handling, choosing a component/design-system approach, or a general
visual redesign pass — use the `taste-skill` skill installed at
`.claude/skills/taste-skill/SKILL.md`. It covers picking the right design
system for the kind of site this is, dark-mode token strategy, avoiding a
generic "AI slop" SaaS look, and other frontend taste conventions.

## Stack

- Jekyll (via the `github-pages` gem, so it matches GitHub's actual Pages build
  environment) + `remote_theme: artemsheludko/flexible-jekyll`.
- The theme is pulled in remotely (not vendored into the repo). We only keep
  **local override copies** of the specific theme files we've customized:
  - `_layouts/main.html` — sidebar (avatar, bio, nav, contact icons, footer).
    Also renders `_includes/construction-banner.html` near the top of
    `.content-box`, but only on individual project pages (`page.collection ==
    "projects"`) — not the homepage, about, resume, or posters as a whole.
    `index.html` separately renders the same include inside each project
    card's `.post-content`, under the excerpt. Both check the finished list
    against the project's slug, so a project's status only needs to change
    in one place. Shown on every project except the slugs listed in
    `_data/finished_projects.yml` — check that file for the current list
    rather than trusting a snapshot here. Update it as projects get
    finished; remove both includes entirely once nothing is left in
    progress.
  - `_includes/head.html` — `<head>`, meta tags, favicon (points at bio-photo.jpg
    instead of the theme's default icon). Viewport meta is
    `width=device-width, initial-scale=1` — deliberately no `maximum-scale`,
    since that previously blocked pinch-zoom on iOS.
  - `index.html` — homepage template; loops over the `projects` collection
    instead of the theme's default blog-post loop
  Any other theme file (e.g. `_layouts/default.html`) is still coming straight
  from the remote theme — if we ever need to touch one, copy it in as a local
  override first (fetch from `github.com/artemsheludko/flexible-jekyll`)
  rather than editing it in place.

## Repo structure

- `_pages/about.md`, `_pages/resume.md` — standalone content pages.
- `_projects/*.md` — one file per project shown on the homepage. Front matter:
  `title`, `excerpt`, `order` (sort order on homepage — see the note above
  under "Open items" on how it's meant to be chronological), `completed`
  (plain "Month Year" string, rendered pinned to the bottom-right of the
  homepage tile via `.post-date` in `assets/css/custom.css`; omitted
  entirely for projects with no fixed completion date, e.g.
  `kinova-assistive-robotics` which is an ongoing lab position, and for
  `coming-soon`), `img` (thumbnail path, relative to
  `assets/img/projects/`), `img-position` (CSS `background-position`
  for the thumbnail crop — supports percentages like `40% 50%` or edge-offset
  syntax like `left 20px top 10px`). Both `img` and `img-position` ship
  commented out as placeholders on projects that don't have a photo yet —
  uncomment once a file is added.
- `assets/img/projects/<project-slug>/` — one subfolder per project for its
  images (thumbnail + any inline body images). Folder name doesn't need to
  match the project's filename, but we've kept them matching by convention.
- `assets/video/` — video clips referenced from project bodies.
- `assets/files/resume.pdf` / `resume.docx` — Miguel's resume, linked from
  `_pages/resume.md`.
- `assets/css/custom.css` — all our styling additions/overrides on top of the
  theme's `main.css`, linked from the local `_includes/head.html`. Reusable
  classes defined here:
  - `.site-nav ul` — strips bullets from the sidebar nav list.
  - `.resume-embed` — keeps the embedded resume PDF at its true (8.5:11)
    aspect ratio instead of a fixed pixel height, so it doesn't squish on
    mobile.
  - `.img-text-row` — floats media (an `<img>`/`<video>`, or an `.img-pair`/
    `.img-stack` group) to the left of the following text inside a project
    body; text wraps in the space beside it and drops to full width below
    once it runs past the media's bottom edge. All media is left-aligned —
    there is no right-aligned variant. Below a 900px *content-column* width
    (a CSS container query on `.content-box`, not a viewport media query —
    this reacts to the actual space available next to the sidebar, not the
    full page width), media unfloats and stacks above the text instead. That
    threshold is sized off the widest image on the site (500px) plus its
    margin plus a ~350px minimum text-column width, so no row's text column
    gets narrower than that while floating. Note: `@container` measures the
    *content box* (padding excluded) — `.content-box`'s own 280px of padding
    (260px reserved for the sidebar + 20px) caps its content width at
    `1250px wrapper max − 280px = 970px` even at full width, so this
    threshold must stay under ~970px or floating becomes unreachable on any
    screen size —
    raise/lower it in `assets/css/custom.css` to change that minimum. Below
    a 768px *viewport* width (an ordinary `@media` query this time, since at
    that point we're targeting actual phones rather than reacting to
    sidebar layout) media additionally drops to full column width — media
    author sizes like `style="width: 500px;"` are meant as desktop/tablet
    caps, not phone sizes, so this stage forces `width: 100% !important` on
    every image/video inside `.img-text-row`/`.img-pair`/`.img-stack` (the
    `!important` is required to beat those inline styles) and stacks
    `.img-pair` into a column instead of a row. `height` stays `auto`
    throughout so aspect ratios never break. This is also where
    `.content-box.content-box--article { display: block }` is
    re-asserted at doubled specificity, since the theme's own `main.css`
    re-declares `.content-box { display: flex }` inside its identical
    `@media (max-width: 768px)` block — without the specificity bump,
    article pages would fall back to flex layout on phones and every
    paragraph would shrink-wrap to its own text width instead of filling
    the column. Usage:
    ```html
    <div class="img-text-row" markdown="1">
    <img src="/assets/img/projects/<slug>/<file>.jpg" alt="..." style="width: 150px;">

    Text goes here, **markdown works** since of `markdown="1"` on the div.
    </div>
    ```
    Swap the `<img>` for a `<video autoplay loop muted playsinline style="width: ...px;"><source src="..." type="video/mp4"></video>` to embed a looping clip instead. Size is controlled per-element via inline
    `style="width: ...px"` (height is automatic — never set both, or the
    aspect ratio breaks). `markdown="1"` on the wrapping div is required for
    any Markdown syntax inside it (bold, links, `<br>`) to actually render
    instead of showing as literal text.
  - `.img-pair` — pairs with `.img-text-row` to show two images/videos side
    by side next to text (instead of just one). Wrap the pair in a div with
    this class and use that div as the media slot:
    ```html
    <div class="img-text-row" markdown="1">
    <div class="img-pair">
    <img src="/assets/img/projects/<slug>/<file1>.jpg" alt="..." style="width: 150px;">
    <img src="/assets/img/projects/<slug>/<file2>.jpg" alt="..." style="width: 150px;">
    </div>

    Text goes here.
    </div>
    ```
  - `.img-stack` — pairs with `.img-text-row` (or nests inside `.img-pair`)
    to stack two images/videos vertically instead of side by side. Same
    wrapping pattern as `.img-pair`, just stacked in a column.
  - `.content-box img/video/iframe { max-width: 100% }` — belt-and-braces
    mobile guard, separate from the breakpoint logic above. The theme
    already caps `<img>` at 100% width globally, but not `<video>` or
    `<iframe>`, so a clip authored at `style="width: 500px;"` could overflow
    a phone viewport outright; iOS Safari responds to that kind of overflow
    by shrink-to-fitting (zooming out) the *whole page*, which reads as
    "everything tiny and squished" rather than one broken element. This
    rule removes that failure mode regardless of where the media sits on
    the page.
  - `.construction-banner` — the amber notice box rendered by
    `_includes/construction-banner.html` (see `_layouts/main.html` above).
    Not meant to be used directly in page/project markdown.
  - `.content-box--article h2` / `ul` / `li` — gives Markdown `##` headings
    and bullet lists a styled look (PT Serif, navy accent, bottom-rule under
    h2) on article-type pages (`about.md`, `resume.md`, project bodies that
    use headings) — the theme has no styling at all for these, so without
    this they render as bare browser defaults. Project bodies mostly use
    `.section-header` instead of `##` headings, so this mainly affects
    `about.md` today.

## Analytics (GoatCounter)

Page views + outbound-link/download clicks are tracked with
[GoatCounter](https://www.goatcounter.com) (free for personal/non-commercial
sites, no cookie banner needed). Wired into `_includes/head.html`, gated on
`goatcounter-code` in `_config.yml` being non-blank so local dev builds don't
report views.

- **Setup Miguel still needs to do (I can't do this part — needs his email):**
  sign up at https://www.goatcounter.com/signup, pick a site code (e.g.
  `miguel-gcoca`), then put that code into `goatcounter-code:` in
  `_config.yml`. The dashboard lives at
  `https://<code>.goatcounter.com` and is login-only — only Miguel can see it.
- Pageviews are tracked automatically by the script. Clicks on outbound links
  (different hostname) and file downloads (`.pdf`/`.doc(x)`/`.ppt(x)`/`.zip`/
  `.mp4`) are additionally sent as custom events, prefixed `outbound:` /
  `download:` in the GoatCounter dashboard's page list, via the inline click
  handler in `head.html`.
- **Excluding Miguel's own visits from the stats:** GoatCounter's script has
  a built-in per-browser opt-out. Visit the site with `#toggle-goatcounter`
  appended to the URL (e.g. `https://miguel-gcoca.github.io/#toggle-goatcounter`)
  once on each of his own browsers/devices — it flips a `localStorage` flag
  that silently stops sending stats from that browser. Visiting the same URL
  again toggles it back on. This doesn't affect other visitors.

## Local dev workflow

- `bundle exec jekyll serve --host 127.0.0.1 --port 4444` runs the local
  preview at `http://localhost:4444`. WSL2 forwards localhost automatically,
  so it's reachable from the Windows browser with no extra setup.
- Auto-regeneration picks up changes to content/templates/CSS on save — just
  refresh the browser. **`_config.yml` changes require a full server
  restart** (kill it and re-run the serve command); the running process
  doesn't reload that file.
- Run `bundle exec jekyll serve` as a background/tracked process (Claude
  Code's `run_in_background`), not manually detached — it's gotten killed by
  session boundaries a couple of times and needed restarting.

### Known environment quirks (already patched, don't re-debug from scratch)

This WSL2 sandbox runs Ruby 3.2, but `github-pages` gem pins **Jekyll 3.9.0**
and **Liquid 4.0.3** (matching GitHub's actual production build environment,
which is on an older Ruby). Two of those old dependencies call Ruby APIs that
3.2 removed, and both were hand-patched directly in the local
`vendor/bundle/` install (which is gitignored — **never committed, and wiped
out by a fresh `bundle install`**, so if `vendor/` gets deleted/reinstalled
these crashes will come back):

1. `liquid-4.0.3/lib/liquid/variable.rb` — `taint_check` calls
   `obj.tainted?`, which Ruby 3.2 removed entirely. Patched to
   `obj.respond_to?(:tainted?) && obj.tainted?`.
2. `jekyll-3.9.0/lib/jekyll/utils/platforms.rb` — `proc_version` used an old
   `Pathutil#read` call incompatible with Ruby 3.2 keyword-arg handling,
   which crashed `jekyll serve`'s file-watcher specifically on WSL (because
   `/proc/version` contains "microsoft", triggering the `bash_on_windows?`
   codepath). Patched `proc_version` to just use `File.read("/proc/version")`
   directly.

If `bundle exec jekyll serve` starts throwing `NoMethodError: tainted?` or
`TypeError: no implicit conversion of Hash into Integer` again, reapply these
two patches rather than re-diagnosing from scratch. None of this affects the
real GitHub Pages build — it only matters for local preview in this sandbox.

Also: `webrick` is in the `Gemfile` explicitly — Ruby 3.0+ dropped it from
the standard library and `jekyll serve` needs it.

## Git / deploy workflow

- Git identity is configured globally: `Miguel Grisales Coca` /
  `mgrisalescoca@gmail.com`.
- Push auth is handled via `gh` (already authenticated as `Miguel-GCoca`) —
  its credential helper is wired into git, so `git push` just works, no
  token prompts.
- **Never commit or push without being asked explicitly** — Miguel has been
  iterating live against the local preview and often wants several rounds of
  changes reviewed before anything ships. Stage and show a diff summary,
  then wait for a go-ahead.
- Once pushed, GitHub rebuilds and republishes automatically — usually under
  a minute. `gh run list --repo Miguel-GCoca/Miguel-GCoca.github.io` or
  `gh api repos/Miguel-GCoca/Miguel-GCoca.github.io/pages/builds/latest`
  confirm build status if needed instead of just guessing/waiting.

## Bash completion (outside the repo, informational)

Set up in `~/.bashrc` (sources bash-completion) plus two files in
`~/.local/share/bash-completion/completions/`: `bundle` (subcommands +
`bundle exec <gem-executable>` completion by scanning `vendor/bundle`) and
`jekyll` (subcommands + per-subcommand flags). `bundle`'s completion
delegates to `jekyll`'s when it detects `bundle exec jekyll ...`. Not part of
the site itself, just quality-of-life for Miguel's shell.

## Open items as of last session

All projects now have real thumbnails and photos/video except
`soft-bodied-worm`, which is genuinely still a placeholder (empty image
folder, body references `PLACEHOLDER-1.jpg`/`PLACEHOLDER-2.jpg` — actual
broken images, not just a missing thumbnail). Miguel's explicit call
(2026-08-27): leave it as-is for now, don't revisit unless he brings it up.

Homepage `order` values are meant to be strict reverse-chronological by each
project's "Completed" date (2026-09-13 pass fixed a stale ordering and two
wrong years found along the way: `multimodal-sensing-system` was actually
completed September **2023**, not 2022, and `dynamic-swept-wing` April
**2025**, not 2024 — both corrected in the project body text too). Miguel
explicitly chose strict chronological over keeping the previous
publication-based promotion of `multimodal-sensing-system` into the top-4
row — don't reintroduce that promotion without asking him again.

Mid-way through a full content/copy review of the projects + About page,
aimed at making the portfolio job-ready (MIT CommLab's engineering
portfolio guide was used as a structural reference). A first pass of fixes
is already made in the working tree but **uncommitted** — typo corrections
across several project pages, the `dynamic-swept-wing` construction-banner
bug (it's finished but was missing from `finished_projects.yml`), a new
"Technical Lead" role section + 14-DOF stat on
`bring-roar-to-life`, a new Awards section on `about.md`, and a rewritten
bio + sidebar blurb (`_config.yml` `about-author`) framing Miguel as a
mechatronics generalist who specifically names ROS2, reinforcement
learning, and physical AI (his direction, 2026-08-27) rather than vague
"controls." Check `git diff` before starting new work so it isn't redone;
still needs Miguel's review and go-ahead before committing (per the rule
above — this doesn't change that).

**Needs Miguel's input/material before continuing:**
- **High priority (2026-09-02):** `anky-jr` (ankybot) project page needs a
  new section on failure mode evaluation and analysis. Miguel called this
  imperative to add soon — needs his write-up/content before it can go in.
- About page Skills list hasn't been touched yet. Planned: add
  Fabrication/3D-printing/machining, a standalone "Reinforcement Learning"
  line (currently buried inside "Isaac Lab"), LabVIEW, and Sensor
  integration/signal processing — all already evidenced in the project
  write-ups. Still need from Miguel: confirm Fritzing is the actual
  PCB/schematic tool (a `fritzing.jpg` asset in `bring-roar-to-life`
  suggests it), and whether he uses git for the capstone's ROS2 code.
- No project page yet for the Kinova Gen-3 / Assistive Robotics Lab work
  (his most recent lab position per `resume.pdf`, Sep 2025–Mar 2026) —
  needs his description + photos.
- Outcome numbers, if he has them: `human-augmentation-exosuit`
  (jump-height result), `mechatronic-musical-instrument` (volume
  reduction / MIDI latency), `multimodal-sensing-system` (validation
  accuracy vs. commercial devices, from the *Frontiers in Aging* paper),
  `dynamic-swept-wing` (what the PIV flow test actually showed).
- HAULC/MUHASS poster PDFs, if they exist — `_pages/posters.md` only has 2
  of the 4 posters that have text extracts sitting in `assets/files/`.
- `resume.pdf`/`resume.docx` need manual fixes only Miguel can make (can't
  edit those formats directly): airfoil should read SD7062 not E214,
  sensing project should read PPG not ECG (site is confirmed correct on
  both), plus "coeficient"→coefficient and "dissasembly"→disassembly.

**Ready to do, just needs a go-ahead:**
- Alt text on project images (most `<img>` tags have none).
- Compress video/image assets. `assets/video/` is ~330MB across 17 files
  now, several already committed (including the 88MB `training.mp4` —
  already in git history, so this is no longer a "flag before committing"
  situation, it's a real page-weight concern for site visitors regardless
  of repo size).
- Small write-ins: a "Result" line atop `bring-roar-to-life`, a closing
  sentence on `anky-jr` tying it back to the capstone, a line on
  `dynamic-swept-wing` about the C/C++ controls work the resume credits
  but the site page doesn't mention.
- Cross-link About's Publications entry to the `multimodal-sensing-system`
  project page, and move that project's NIH/publication mention higher up
  its own page (currently a closing aside).
