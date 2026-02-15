# AGENTS.md — Portfolio project guide for AI agents and developers

This file documents the repository layout, how to run the site, and conventions so agents and developers can work on it consistently.

---

## Project overview

- **What it is:** A minimal, light-themed personal portfolio site for **Ivan Inocencio**.
- **Goals:** Introduce the person, show projects, certifications, and capture newsletter signups (form is stubbed; no backend).
- **Primary stack:** Static HTML/CSS at project root. No JavaScript, frameworks, or build tools. Deployable on Cloudflare Pages.
- **Optional stack:** Astro in `src/` for when Node.js is available; not required for day-to-day edits.

---

## Repository layout

| Path | Purpose |
|------|--------|
| `index.html`, `about.html`, `projects.html`, `certifications.html`, `newsletter.html`, `now.html` | Site pages. |
| `styles.css` | Global styles (light theme, typography, components). |
| `assets/images/` | Images. `ivan.jpg` (avatar), `certifications/` for cert images (`cert-<issuer>-<topic>.jpg`). |
| `static/` | Legacy. Contains `styles.css` and `assets/` for Astro build. |
| `local-static/` | Legacy. Old HTML structure. |
| `src/` | Astro app. Build output goes to `dist/`. |
| `start_site.bat` | Starts Python HTTP server from project root and opens browser (requires Python). |
| `Open portfolio (no server).bat` | Opens `index.html` in default browser via `file://` — **no server, no connection errors.** |
| `HOW_TO_VIEW_SITE.txt` | Short user-facing instructions for viewing the site. |

---

## How to view / run the site

### Recommended (no server)

- **Double-click:** `Open portfolio (no server).bat`  
- Opens `index.html` in the default browser via `file://`.  
- No server, no `ERR_CONNECTION_REFUSED`. Use this when the user just wants to see the site.

### With a local server

- **Double-click:** `start_site.bat`  
  - Starts a Python HTTP server in the project root on port 8000 and opens the browser after a short delay.  
  - Uses `py` or `python` (whichever is on PATH). Keep the “Portfolio Server” window open.
- **Or manually:**
  - `cd` to project root
  - `py -m http.server 8000` (or `python -m http.server 8000`)
  - Open `http://127.0.0.1:8000/` in the browser.

### Astro (when Node is available)

- `npm install` then `npm run dev` (or `npm run build` then `npm run preview`).  
- Serves the Astro-built site; not required for the static-only workflow.

---

## Design and theme

- **Theme:** Light. Background `#fff`, surfaces `#fafafa`, borders `#e5e5e5`, text `#000`, muted `#525252`.
- **Accent:** Violent red `#b91c1c` for links, CTAs, highlights, hover/focus only.
- **Fonts:** Switzer (body), Khand 700 (headings); loaded via Fontshare and Google Fonts.
- **Style:** Minimal, professional, mobile-first. Max-width container, consistent section rhythm.

---

## Debug and connection issues

- **Symptom:** Browser shows `ERR_CONNECTION_REFUSED` at `http://127.0.0.1:8000/`.  
- **Cause:** No process is listening on that URL (server was never started, or wrong port/URL).  
- **Fix for users:** Prefer **`Open portfolio (no server).bat`** so no server is needed.  
- **If a server is required:** Use **`start_site.bat`** (or run `py -m http.server 8000` from project root) and then open `http://127.0.0.1:8000/`.  
- **For agents debugging:** Run `py serve_debug.py` from the repo root. It serves `static/` and writes logs to `.cursor/debug.log` (NDJSON) so you can confirm server start and request receipt.

---

## Conventions for agents

1. **Deploy root:** The project root (`index.html`, `styles.css`, `assets/`) deploys to Cloudflare Pages. Use relative paths for compatibility with both `file://` and HTTP.
2. **Assets:** Put images in `assets/images/`. Certifications: `assets/images/certifications/cert-<issuer>-<topic>.jpg` (lowercase, hyphens only).
3. **Newsletter form:** HTML-only; comment in code for later wiring to Buttondown, ConvertKit, etc.
4. **No backend:** Newsletter form is non-functional by design; no auth, database, or API.  
5. **No JavaScript:** HTML + CSS only. No frameworks or build tools.

---

## Quick reference

- **View site (no server):** Run `Open portfolio (no server).bat`.  
- **View site (with server):** Run `start_site.bat` or `py -m http.server 8000` from project root, then open `http://127.0.0.1:8000/`.  
- **Styles:** `styles.css` (project root).  
- **Deploy:** Upload project root to Cloudflare Pages or connect Git repo.  
- **User instructions:** `HOW_TO_VIEW_SITE.txt`.
