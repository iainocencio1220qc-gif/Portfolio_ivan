# AGENTS.md — Portfolio project guide for AI agents and developers

This file documents the repository layout, how to run the site, and conventions so agents and developers can work on it consistently.

---

## Project overview

- **What it is:** A minimal, dark-themed personal portfolio site for **Ivan Inocencio**.
- **Goals:** Introduce the person, show projects, and capture newsletter signups (form is stubbed; no backend).
- **Primary stack in use:** Static HTML/CSS in `static/`. No server required for local viewing.
- **Optional stack:** Astro in `src/` for when Node.js is available; not required for day-to-day edits.

---

## Repository layout

| Path | Purpose |
|------|--------|
| `static/` | **Shared assets for build and no-server viewing.** Contains `styles.css` and `assets/` only (no HTML). |
| `static/styles.css` | Global styles (dark theme, typography, components). |
| `static/assets/` | Images (e.g. `ivan.jpg`). |
| `local-static/` | **Static HTML for no-server viewing.** Home, about, projects; references `../static/` for CSS and assets. |
| `src/` | Astro app. Build output goes to `dist/`; **deployed site uses this** (no overwrite from static HTML). |
| `start_site.bat` | Starts Python HTTP server from `static/` and opens browser (requires Python). |
| `Open portfolio (no server).bat` | Opens `local-static/index.html` in default browser via `file://` — **no server, no connection errors.** |
| `serve_debug.py` | Debug server that serves `static/` and writes NDJSON logs to `.cursor/debug.log` for diagnosing connection issues. |
| `HOW_TO_VIEW_SITE.txt` | Short user-facing instructions for viewing the site. |

---

## How to view / run the site

### Recommended (no server)

- **Double-click:** `Open portfolio (no server).bat`  
- Opens `local-static/index.html` in the default browser via `file://`.  
- No server, no `ERR_CONNECTION_REFUSED`. Use this when the user just wants to see the site.

### With a local server

- **Double-click:** `start_site.bat`  
  - Starts a Python HTTP server in `static/` on port 8000 and opens the browser after a short delay.  
  - Uses `py` or `python` (whichever is on PATH). Keep the “Portfolio Server” window open.
- **Or manually:**
  - `cd static`
  - `py -m http.server 8000` (or `python -m http.server 8000`)
  - Open `http://127.0.0.1:8000/` in the browser.

### Astro (when Node is available)

- `npm install` then `npm run dev` (or `npm run build` then `npm run preview`).  
- Serves the Astro-built site; not required for the static-only workflow.

---

## Design and theme

- **Theme:** Dark. Background `#0b0b0b`, surfaces `#111`, borders `#242424`, text `#f4f4f4`, muted `#cfcfcf`.
- **Accent:** Red `#a00` for links, CTAs, and emphasis (no extra colors).
- **Fonts:** Switzer (body), Khand 700 (headings); loaded via Fontshare and Google Fonts.
- **Style:** Minimal, professional, strong typography and spacing. No gradients; subtle vignette on `body` only.

---

## Debug and connection issues

- **Symptom:** Browser shows `ERR_CONNECTION_REFUSED` at `http://127.0.0.1:8000/`.  
- **Cause:** No process is listening on that URL (server was never started, or wrong port/URL).  
- **Fix for users:** Prefer **`Open portfolio (no server).bat`** so no server is needed.  
- **If a server is required:** Use **`start_site.bat`** (or run `py -m http.server 8000` from `static/`) and then open `http://127.0.0.1:8000/`.  
- **For agents debugging:** Run `py serve_debug.py` from the repo root. It serves `static/` and writes logs to `.cursor/debug.log` (NDJSON) so you can confirm server start and request receipt.

---

## Conventions for agents

1. **Deployment uses Astro build.** The built site in `dist/` (from `src/`) is what gets deployed; `static/` only contributes `styles.css` and `assets/` to the build. Keep `src/` and `local-static/` in sync for design changes.
2. **Assets:** Put images in `static/assets/`. In Astro pages use root-relative paths (e.g. `/assets/ivan.jpg`). In `local-static/` use `../static/assets/ivan.jpg`.
3. **Placeholder content:** Keep or mark placeholder copy with `[PLACEHOLDER]` so it’s easy to find and replace later.
4. **No backend:** Newsletter form is non-functional by design; no auth, database, or API.  
5. **Launchers:** Do not remove `Open portfolio (no server).bat` or `start_site.bat` without providing an equivalent way to view the site; prefer updating `HOW_TO_VIEW_SITE.txt` and this file.

---

## Quick reference

- **View site (no server):** Run `Open portfolio (no server).bat`.  
- **View site (with server):** Run `start_site.bat` or `py -m http.server 8000` from `static/` then open `http://127.0.0.1:8000/`.  
- **Styles:** `static/styles.css`.  
- **Home (no server):** `local-static/index.html`. **Deployed:** Astro build from `src/` → `dist/`.  
- **User instructions:** `HOW_TO_VIEW_SITE.txt`.
