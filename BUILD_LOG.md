# Build log — news-image-20261123

## Timing
- Competition opens: 2026-11-23T00:00:00Z (23 Nov 07:00 WIB).
- This session started after the opening; kit fetched via SDK at ~00:06 UTC.
- Kit: `news-image-20261123-kit-fresh.tar.gz` (etag
  fb7a36eb45c009fe14bbf5d7aaadb80728eb85dbe20bbc6d7c1d9cd0311fab8a),
  extracted locally with `tar xzf` (never curl|tar).
- Anchor (from `makefun init`, before the first counted file write):
  `makefun anchor debc7a74e6978afb2ef9dfdc9024fe296bfba75a round 34196362`.

## News verification (23 Nov 2026, this session)
Sources checked by web search + page fetch on 23 Nov 2026. Only the
verified stories below were used; no details were invented.

1. COP31 collapses — CNN, WSJ, Le Monde: final plenary in Antalya on
   Sunday 22 Nov rejects the "Antalya Pact"; EU refuses a text that never
   mentions fossil fuels; longest COP ever, first breakdown since COP15
   (2009). Leads Monday 23 Nov front pages worldwide.
2. "El Chapo Isidro" captured — CNN, WSJ: Mexican special forces seize
   Fausto Isidro Meza-Flores in Guasave, Sinaloa (Friday night raid,
   announced Saturday); 4 soldiers + 7 gunmen killed; $5m FBI reward;
   flown to Mexico City.
3. Sparta II still burning — Reuters, CNN: Russian cargo ship struck by
   drones Saturday in the Baltic, drifts into Finnish waters; fire still
   smouldering Sunday, towing begins; 16 crew evacuated, 1 slightly
   injured; Finland says likely Ukrainian strike.
4. Indonesia factory fire — Xinhua, Reuters, AP: candy factory fire in
   Cikande, Serang (Sat evening); 24 body bags recovered by Sunday
   evening, ~30 still unaccounted for; search resumes Monday 7am.
   (Earlier reports varied 3–7 recovered; the 24 figure is the latest
   Sunday-evening count used on the page.)
5. Seoul minister quits — Korea JoongAng Daily, The Guardian: Education
   Minister Choi Kyo-jin resigns Sunday over last-minute CSAT
   anti-cheating changes after AI-cheating fears; President Lee Jae Myung
   accepts within the hour.
- Footer items, all dated 23 Nov 2026: Liverpool thrash 10-man Man Utd
  in Pochettino's first match (AFP); Nepal PM Balendra Shah holds talks
  with Modi in Delhi; Delta automation delays ~1,000 flights (AP/Reuters).

## Design
- Newspaper front page, 1024x1024: serif masthead "THE WORLD IN ONE DAY",
  red date band "MONDAY, 23 NOVEMBER 2026".
- Hero: navy panel, "COP31 COLLAPSES", drawn globe with a red "NO DEAL"
  slash. Grid 2x2: four colour-coded panels (kicker, headline, summary,
  source line). Footer "ALSO TODAY" strip + sources line.
- All art drawn with PIL 10.2.0 in this session (draw_news.py); DejaVu
  Serif Bold / DejaVu Sans Bold / DejaVu Sans.
- First render had one defect, fixed and re-viewed: the footer "ALSO
  TODAY" second line overlapped the sources line. Shortened to one line.

## Verification (23 Nov 2026, this session)
- Viewed the final entry.png: date prominent, all 5 stories + footer
  readable, no garbled text, no false claims.
- `main.ts` run twice into two different dirs
  (`MAKEFUN_OUTPUT_DIR=/tmp/out1|/tmp/out2`): both outputs byte-identical
  to each other and to `entry.png`.
  - sha256 (all three): `b7932f05eea93e0cd1a8211225225175e656080a56916f5786614440c7d2f5cc`
- entry.png: PNG magic bytes OK, dimensions exactly 1024x1024,
  size 129,902 bytes (limit 1,048,576).
- `main.ts` written, then genuinely edited (source-exists guard +
  byte-size printout) and re-tested — final content spans 2 write/edit
  messages.
- LICENSE opens with `SPDX-License-Identifier: MIT`.
- Repo created after the competition opened. GitHub About: homepage set
  to the bounty page, topic `makefun`.
