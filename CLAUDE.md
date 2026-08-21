# Miguel Grisales Coca — Portfolio Site

Personal portfolio for Miguel Grisales Coca, hosted on GitHub Pages at
`https://miguel-gcoca.github.io/`. Repo: `Miguel-GCoca/Miguel-GCoca.github.io`
(user-site repo, so Pages serves straight from `main`, no gh-pages branch needed).

Miguel is a Mechanical Engineering student at UCF (robotics/physical AI focus).
He's actively learning Jekyll/git/web dev through this project — when making
changes, prefer explaining the mechanism (which file, why) over just doing it
silently, and keep edits scoped to what was asked.

## Stack

- Jekyll (via the `github-pages` gem, so it matches GitHub's actual Pages build
  environment) + `remote_theme: artemsheludko/flexible-jekyll`.
- The theme is pulled in remotely (not vendored into the repo). We only keep
  **local override copies** of the specific theme files we've customized:
  - `_layouts/main.html` — sidebar (avatar, bio, nav, contact icons, footer).
    Also renders `_includes/construction-banner.html` near the top of
    `.content-box` on every page except the ones named in its `{% unless %}`
    exclusion list (currently `/resume/` and the Bring ROAR to Life project,
    since those are the only pages considered finished as of this writing).
    Update that list as pages get finished; remove the include entirely once
    nothing is left in progress. The banner is `flex: 0 0 100%` in
    `custom.css` specifically so it forces its own row above the homepage's
    flex/wrap project-card grid instead of sizing like a card.
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
  `title`, `excerpt`, `order` (sort order on homepage), `img` (thumbnail path,
  relative to `assets/img/projects/`), `img-position` (CSS `background-position`
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

- `assets/video/siminloop.MP4` (49MB) and `assets/video/training.mp4` (88MB)
  are sitting untracked — `training.mp4` is now referenced from
  `bring-roar-to-life.md`. **Flag before committing these**: 88MB is close to
  GitHub's 100MB hard file-size limit, and both together (~137MB) will bloat
  the repo permanently (large binaries in git history are painful to remove
  later) and slow down page load for site visitors. Worth suggesting
  compression/trimming before they go in, if not already discussed.
- `anky_irl.jpg` and `team_photo.jpg` are sitting in
  `assets/img/projects/bring-roar-to-life/` unused — Miguel said he'd figure
  out their placement himself.
- Most other projects (`airfoil-inspired-car`, `ankle-perturbation-system`,
  `dynamic-swept-wing`, `human-augmentation-exosuit`,
  `mechatronic-musical-instrument`, `multimodal-sensing-system`,
  `soft-bodied-worm`) still have `img`/`img-position` commented out — no
  thumbnails added yet, folders exist but are empty (and therefore untracked
  by git until something's placed in them).
- There's a stray unfinished bullet ("pushed perturbationsXX") in
  `bring-roar-to-life.md` — looks like a mid-edit placeholder Miguel left,
  not something to silently clean up.
