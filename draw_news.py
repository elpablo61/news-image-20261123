#!/usr/bin/env python3
"""Draw the news-image-20261123 front page: THE WORLD IN ONE DAY.

Newspaper front page, 1024x1024, five verified stories from Monday
23 November 2026 (verified from CNN, Reuters, AP, AFP, WSJ, Le Monde,
Xinhua and Korea JoongAng Daily in this session). All art is drawn
fresh here with PIL; no external images.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (20, 38, 63)
GOLD = (212, 175, 55)
GREY = (90, 90, 88)
LIGHT = (255, 255, 255)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=3)

# ---- Masthead -------------------------------------------------------
d.text((W // 2, 34), "THE WORLD IN ONE DAY", font=font(SERIF, 58),
       fill=INK, anchor="ma")
d.line([40, 108, W - 40, 108], fill=INK, width=2)
d.text((W // 2, 116), "MONDAY, 23 NOVEMBER 2026", font=font(SANS_B, 30),
       fill=RED, anchor="ma")
d.text((W // 2, 152), "THE WORLD'S NEWS IN ONE IMAGE  ·  FIVE STORIES FROM ONE DAY",
       font=font(SANS, 15), fill=GREY, anchor="ma")
d.line([40, 178, W - 40, 178], fill=INK, width=2)

# ---- Hero: COP31 ----------------------------------------------------
hx, hy, hw, hh = 24, 190, 976, 268
d.rectangle([hx, hy, hx + hw, hy + hh], fill=NAVY)
d.rectangle([hx, hy, hx + hw, hy + hh], outline=INK, width=2)
d.text((hx + 22, hy + 14), "CLIMATE  ·  ANTALYA, TURKEY",
       font=font(SANS_B, 17), fill=GOLD)
d.text((hx + 22, hy + 42), "COP31 COLLAPSES", font=font(SERIF, 56), fill=LIGHT)
d.text((hx + 22, hy + 112), "No deal on fossil fuels as talks end in disarray",
       font=font(SERIF_R, 24), fill=(220, 225, 235))
hero_body = (
    "After two weeks of talks, the UN climate summit collapses \u2014 the first "
    "failure to agree an overarching deal since 2009. The EU and others "
    "reject a final text that never names fossil fuels.")
lines = wrap(d, hero_body, font(SANS, 19), 600)
text_block(d, hx + 22, hy + 152, lines, font(SANS, 19), (205, 212, 224), 25)
d.text((hx + 22, hy + hh - 28), "CNN  ·  WALL STREET JOURNAL  ·  LE MONDE",
       font=font(SANS, 13), fill=(170, 180, 195))
# Drawn globe, right side of hero
cx, cy, r = hx + hw - 115, hy + 150, 78
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=4)
d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=GOLD, width=2)
d.line([cx - r, cy, cx + r, cy], fill=GOLD, width=2)
d.arc([cx - r + 12, cy - r + 26, cx + r - 12, cy + r - 26], 200, 340,
      fill=GOLD, width=2)
d.line([cx - 52, cy - 52, cx + 52, cy + 52], fill=RED, width=5)
d.text((cx, cy + r + 10), "NO DEAL", font=font(SANS_B, 16), fill=RED,
       anchor="ma")

# ---- Four story panels ----------------------------------------------
panels = [
    dict(
        x=24, y=474, w=481, h=212, kicker="MEXICO  ·  ORGANISED CRIME",
        color=(139, 0, 0),
        headline="\u201cEL CHAPO ISIDRO\u201d CAPTURED",
        body=("Mexican troops seize Fausto Isidro Meza-Flores, an FBI Ten "
              "Most Wanted fugitive, in Sinaloa. Eleven people are killed "
              "in the raid; the cartel boss is flown to Mexico City."),
        source="CNN  ·  WALL STREET JOURNAL",
    ),
    dict(
        x=519, y=474, w=481, h=212, kicker="BALTIC SEA  ·  UKRAINE WAR",
        color=(31, 78, 121),
        headline="RUSSIAN SHIP STILL BURNING",
        body=("The Sparta II, a sanctioned Russian cargo ship hit by drones "
              "in the Baltic, smoulders off Finland as towing begins. Its "
              "16 crew were evacuated; Finland blames a likely Ukrainian "
              "strike."),
        source="REUTERS  ·  CNN",
    ),
    dict(
        x=24, y=700, w=481, h=212, kicker="INDONESIA  ·  DISASTER",
        color=(204, 85, 0),
        headline="FACTORY FIRE SEARCH RESUMES",
        body=("Rescuers return to a burnt-out candy factory in Cikande, "
              "Indonesia. Twenty-four body bags were recovered by Sunday "
              "evening; about 30 workers are still unaccounted for."),
        source="XINHUA  ·  REUTERS",
    ),
    dict(
        x=519, y=700, w=481, h=212, kicker="SOUTH KOREA  ·  EDUCATION",
        color=(0, 110, 110),
        headline="SEOUL MINISTER QUITS OVER AI-CHEAT ROW",
        body=("Education minister Choi Kyo-jin resigns over last-minute "
              "anti-cheating rules for the national college exam, after "
              "AI-assisted cheating fears. President Lee accepts within "
              "the hour."),
        source="KOREA JOONGANG DAILY  ·  THE GUARDIAN",
    ),
]

for p in panels:
    d.rectangle([p["x"], p["y"], p["x"] + p["w"], p["y"] + p["h"]],
                fill=LIGHT, outline=INK, width=2)
    d.rectangle([p["x"], p["y"], p["x"] + p["w"], p["y"] + 30],
                fill=p["color"])
    d.text((p["x"] + 12, p["y"] + 6), p["kicker"], font=font(SANS_B, 14),
           fill=LIGHT)
    y = p["y"] + 40
    hl = wrap(d, p["headline"], font(SERIF, 25), p["w"] - 24)
    y = text_block(d, p["x"] + 12, y, hl, font(SERIF, 25), INK, 30)
    bl = wrap(d, p["body"], font(SANS, 16), p["w"] - 24)
    y = text_block(d, p["x"] + 12, y + 4, bl, font(SANS, 16),
                   (40, 40, 40), 21)
    d.text((p["x"] + 12, p["y"] + p["h"] - 24), p["source"],
           font=font(SANS, 12), fill=GREY)

# ---- Footer: also today ----------------------------------------------
fy = 928
d.line([40, fy, W - 40, fy], fill=INK, width=2)
d.text((40, fy + 10), "ALSO TODAY", font=font(SANS_B, 15), fill=RED)
also = ("Liverpool thrash 10-man Man Utd  ·  "
        "Nepal PM Shah meets Modi in Delhi  ·  "
        "Delta delays hit Thanksgiving travel")
al = wrap(d, also, font(SANS, 14), W - 80)
text_block(d, 40, fy + 32, al, font(SANS, 14), INK, 19)
d.text((W // 2, H - 34),
       "Stories reported 22\u201323 November 2026  ·  Sources: CNN, Reuters, AP, AFP, WSJ, Le Monde, Xinhua, Korea JoongAng Daily",
       font=font(SANS, 12), fill=GREY, anchor="ma")

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png", img.size)
