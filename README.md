# Let the Whale Breach

Official marketing & dev-log website for **Let the Whale Breach** — a warm,
healing, pixel-art indie game that blends management simulation, community
building, role-playing, and adventure.

## About the Game

A century ago, a brutal war reduced this land to ruins. Now, as the community's
**Delegate**, you return with ambitious workers and artisans who have grown
tired of the kingdom's oppression. Together you rebuild a home from abandoned
wreckage, forge deep bonds with NPCs whose personal histories are woven into
the land, and decide how the new community confronts the kingdom's tyranny.

Rather than a "capitalist efficiency" loop, the core experience empowers the
player as a creative town leader, driven by unique NPC relationships and a
compelling overarching story.

### Core Pillars

- **Personalization & NPC Cooperation** — NPCs voluntarily cover the chores you
  dislike, so you can focus on the activities you truly enjoy.
- **Deep Economic Progression** — Move from unstable "Kingdom Coins" to leading
  a regional "New Community Currency" system.
- **Dual-Mode Fishing** — A relaxed Pomodoro-style "Calm Fishing" mode and a
  first-person "Immersive Fishing" mode with strategic trade-offs.
- **Dynamic NPC System** — NPCs have proficiencies, relationships, conflicts,
  and learn from each other and from the player.
- **Strategic Community Construction** — Restore landmarks (school, tavern,
  hospital) and core production sites that shape the long-term story.
- **Cozy but Meaningful** — A warm pace with real management, strategy, and
  anti-kingdom challenges.

## Repository Contents

This repo contains the static website used to introduce the game and publish
development updates:

- `index.html` — Landing page (story, player role, features, gallery, devlog
  preview).
- `devlog.html` — Full development log / blog page.
- `style.css` — Shared styles for both pages.
- `script.js` — Multi-language switching (EN / 中文 / FR) and shared UI logic.

### Run Locally

It is a plain static site, so any local server works. For example:

```bash
# Python 3
python -m http.server 8000
```

Then open <http://localhost:8000/> in your browser.

### Update Dev Log From Markdown

The full Dev Log page can be generated from `devlog-source.md`.

Log entries default to Chinese. After each dated block, optional `@en` / `@fr` sections hold English and French with the same structure (`Title:` / `Titre :`, `Content`, `Related files` / `Fichiers`, `Note` / `Remarque`). The site switches language via the navbar; those blocks use `html[lang="..."]` in CSS together with `<div class="devlog-lang">`.

1. Edit `devlog-source.md` only.
2. Run:

```bash
python tools/update_devlog.py
```

This command updates both `devlog.html` (timeline + full entries) and `index.html` (homepage devlog preview cards).

## Roadmap

1. **Launch the "Prologue" Demo** — Complete and publicly release a 15–20 minute
   "Prologue" demo for *Let the Whale Breach* on Steam and itch.io to showcase
   the unique "psychological sanctuary" with NPC collaboration and emotional
   connection systems.
2. **Multi-Platform Market Validation** — Convert existing community engagement
   (e.g. Xiaohongshu / Red Notes) into measurable validation through a targeted
   demo launch campaign, paid promotion, and YouTuber / streamer outreach.
   Target: **10,000 Steam Wishlists within three months** of launch.
3. **Secure Key Talent & Prepare for Seed Funding** — Use demo success and
   market data to secure a lead artist and composer, build a full business
   plan and pitch deck, and apply for Ontario-based grants (e.g. OIDMTC) to
   scale the studio.

## Community

- 💬 Discord: <https://discord.gg/HMEXESt38m>
- 📕 Red Notes (Xiaohongshu): coming soon

We welcome feedback, ideas, and travelers willing to help the whale breach.
