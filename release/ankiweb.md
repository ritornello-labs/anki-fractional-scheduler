---
title: Fractional New-Card Scheduler
support_url: https://github.com/ritornello-labs/anki-fractional-scheduler
---

Fractional New-Card Scheduler lets you pace new cards below whole-number daily limits, such as introducing 1 new card every 3 days, while still using Anki's Today-only new-card limits.

## See it in Anki

![Language trickle schedule with a 14-day preview across four populated subdecks](https://ritornello.dev/media/ankiweb/2026-09-23-v5/fractional-scheduler/gallery-01.png)

![One new card every three days and balance-first scheduling](https://ritornello.dev/media/ankiweb/2026-09-23-v5/fractional-scheduler/gallery-02.png)

![Targets pane selecting the nested language decks](https://ritornello.dev/media/ankiweb/2026-09-23-v5/fractional-scheduler/gallery-03.png)

![Balance queue pane spreading new cards across matching subdecks](https://ritornello.dev/media/ankiweb/2026-09-23-v5/fractional-scheduler/gallery-04.png)

![Global settings pane for fractional scheduling](https://ritornello.dev/media/ankiweb/2026-09-23-v5/fractional-scheduler/gallery-05.png)

![Nested decks in Anki with current new-card counts](https://ritornello.dev/media/ankiweb/2026-09-23-v5/fractional-scheduler/gallery-06.png)

Use it when some decks deserve a slow trickle of new material instead of a fixed whole number every day. The add-on can target exact decks or wildcard deck groups, preview the next 14 days, and apply the resulting Today-only limits automatically on profile open, collection open, or before sync.

It also includes deck health badges: schedule rules can mark decks when a deck or its monitored descendants are blocked by 0/day limits or have no unsuspended new cards available.

Features:

- Every-N-days schedules, including fractional patterns like 1 every 3 days.
- Day-of-week schedules with separate values for Monday through Sunday.
- Multiple exact or wildcard deck targets per schedule.
- Exact targets follow their deck through direct and parent-deck renames.
- Stable staggering so related decks can be spread across different days.
- Balance-first scheduling for grouped decks, designed to avoid catch-up spikes.
- Optional notify badges per schedule.
- A config dialog with schedule editing, target picking, and preview tables.

Requires Anki 2.1.55 or newer.

GitHub: [https://github.com/ritornello-labs/anki-fractional-scheduler](https://github.com/ritornello-labs/anki-fractional-scheduler)

Support continued development: [ritornello.dev/support](https://ritornello.dev/support).
