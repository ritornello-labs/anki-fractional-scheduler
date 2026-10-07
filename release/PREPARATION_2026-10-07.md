# Listing preparation — 2026-10-07

Status: prepared for review; **awaiting explicit image/copy approval**. No AnkiWeb submission or public media upload in this pass.

The complete local review hub and native capture sources are recorded in the private workspace publication queue. GIFs use actual Anki 25.09 workbench captures from disposable profiles. Similar question/answer demos hold the question for two seconds and answer for three; interactive demos allow time for actions and feedback.

Every listing includes the Ritornello banner, gallery invitation, stable support page, and the public GitHub URL where a dedicated public repository exists. Videos are absent.

## Exact proposed listings

### Fractional New-Card Scheduler

- Listing: `release/ankiweb.md`
- Copy SHA-256: `002ef730fb4049aa7313ca59d7936138ec364a518d2279377179b49232f9efbd`
- Candidate SHA-256: `acda70662692c2e522860b964e4955707ef09b99274095cb0a5e26fcb29bcbcb`
- Approval: awaiting approval
- GIF `fractional-scheduler/schedule.gif`: `8a9b26b66d8a1bb494078d45c8124180339e9cb571a14cdc17f9e36a3a5c9bdc`

## Upload procedure

1. Record explicit approval against these exact copy and image hashes. Any subsequent visible change requires fresh review.
2. Verify the current quota and exact original share/deck name. Open only the isolated Publisher when an export/import is needed; never operate the personal profile.
3. Wait for Elvis if 1Password or account authentication requires interaction. The scheduled reminder only pings him; it never publishes automatically.
4. Publish through `anki-addon-release`; owner-verify the listing and download its delivered artifact.
5. Attach the exact submitted/delivered bytes to a tagged GitHub release, verify its digest, and update the website gallery/release links and workspace queue.

For add-ons installed directly from GitHub release files, release notes must explain that they do not auto-update; AnkiWeb installs do.

## Verification

50 tests passed (one environment-dependent skip); current populated native config rendered across Basics, Rule and Targets/balance panes. Added `.tmp/` to ignores so generated disposable profiles remain outside release source. Archive manifest/hygiene passed.
