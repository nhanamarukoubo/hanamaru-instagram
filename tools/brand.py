#!/usr/bin/env python3
"""はなまる工房 ブランド素材(マスコット・はなまる・星・ハート)をSVG文字列で返す。
使い方: from brand import mascot, hanamaru, star, heart
  mascot("rabbit"|"bear"|"chick"|"cat") -> SVG(viewBox 0 0 100 100、幅高さはCSSで指定)
  hanamaru(size_mm, color="#ef5b5b") / star(color, size_mm, rot) / heart(color, size_mm, rot)
"""
INK = "#5b4636"

# 行ごとのデータ: (行の名前, テーマ色, 薄い色, マスコット, ひとこと, [(字, ことば, 絵文字)])
LINES = [
    ("あ", "#f28fa8", "#fde8ee", "rabbit", "いっしょに かこうね！", [
        ("あ", "あり", "ant"), ("い", "いぬ", "dog-face"), ("う", "うさぎ", "rabbit-face"),
        ("え", "えんぴつ", "pencil"), ("お", "おにぎり", "rice-ball")]),
    ("か", "#f6a65a", "#fff0e0", "bear", "ゆっくり ていねいにね", [
        ("か", "かさ", "umbrella"), ("き", "きのこ", "mushroom"), ("く", "くま", "bear"),
        ("け", "けむし", "bug"), ("こ", "こいのぼり", "carp-streamer")]),
    ("さ", "#e8c33c", "#fdf6d8", "chick", "ぴよっ！ がんばろう", [
        ("さ", "さかな", "fish"), ("し", "しか", "deer"), ("す", "すいか", "watermelon"),
        ("せ", "せっけん", "soap"), ("そ", "そり", "sled")]),
    ("た", "#7cc47f", "#e6f5e3", "cat", "とめ・はねに ちゅうい！", [
        ("た", "たまご", "egg"), ("ち", "ちょう", "butterfly"), ("つ", "つき", "crescent-moon"),
        ("て", "てぶくろ", "gloves"), ("と", "とまと", "tomato")]),
    ("な", "#5fbfc0", "#e0f4f3", "rabbit", "じょうずに なってきたね", [
        ("な", "なす", "eggplant"), ("に", "にんじん", "carrot"), ("ぬ", "ぬいぐるみ", "teddy-bear"),
        ("ね", "ねこ", "cat-face"), ("の", "のみもの", "cup-with-straw")]),
    ("は", "#6fa8dc", "#e3eefa", "bear", "はんぶん まで きたよ！", [
        ("は", "はな", "tulip"), ("ひ", "ひよこ", "baby-chick"), ("ふ", "ふうせん", "balloon"),
        ("へ", "へび", "snake"), ("ほ", "ほし", "star")]),
    ("ま", "#9d8fe0", "#ece9fb", "chick", "まるい ところは ゆっくり", [
        ("ま", "まど", "window"), ("み", "みかん", "tangerine"), ("む", "むし", "lady-beetle"),
        ("め", "めがね", "glasses"), ("も", "もも", "peach")]),
    ("や", "#d78bd6", "#f8e8f8", "cat", "あと すこしだよ！", [
        ("や", "やま", "snow-capped-mountain"), ("ゆ", "ゆきだるま", "snowman"), ("よ", "よる", "night-with-stars")]),
    ("ら", "#ef8a7e", "#fde6e2", "rabbit", "すごい すごい！", [
        ("ら", "らっぱ", "trumpet"), ("り", "りんご", "red-apple"), ("る", "くるま", "automobile"),
        ("れ", "れもん", "lemon"), ("ろ", "ろうそく", "candle")]),
    ("わ", "#8cc8a8", "#e4f4eb", "bear", "さいごの いちまい！", [
        ("わ", "わに", "crocodile"), ("を", "ほんを よむ", "open-book"), ("ん", "ぱん", "bread")]),
]

# 3文字の行のおまけ「ことばを なぞろう」
BONUS = {"や": ["やま", "ゆき"], "わ": ["わに", "ぱん"]}

# ---------------------------------------------------------------- マスコット
def face(blush="#f7a8b8"):
    return f'''
      <ellipse cx="36" cy="62" rx="4.2" ry="5" fill="{INK}"/>
      <ellipse cx="64" cy="62" rx="4.2" ry="5" fill="{INK}"/>
      <circle cx="37.4" cy="60.2" r="1.6" fill="#fff"/>
      <circle cx="65.4" cy="60.2" r="1.6" fill="#fff"/>
      <ellipse cx="27" cy="71" rx="6" ry="3.6" fill="{blush}" opacity=".85"/>
      <ellipse cx="73" cy="71" rx="6" ry="3.6" fill="{blush}" opacity=".85"/>
      <path d="M44 70 q3 4 6 0 q3 4 6 0" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>'''

def mascot(kind):
    s = f'stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"'
    if kind == "rabbit":
        body = f'''
      <ellipse cx="36" cy="26" rx="9" ry="22" fill="#fff" {s} transform="rotate(-10 36 26)"/>
      <ellipse cx="36" cy="28" rx="4" ry="15" fill="#f9c5d1" transform="rotate(-10 36 28)"/>
      <ellipse cx="64" cy="26" rx="9" ry="22" fill="#fff" {s} transform="rotate(10 64 26)"/>
      <ellipse cx="64" cy="28" rx="4" ry="15" fill="#f9c5d1" transform="rotate(10 64 28)"/>
      <ellipse cx="50" cy="64" rx="34" ry="29" fill="#fff" {s}/>
      <circle cx="73" cy="40" r="5" fill="#f28fa8" {s}/>'''
    elif kind == "bear":
        body = f'''
      <circle cx="22" cy="38" r="12" fill="#d39b6a" {s}/><circle cx="22" cy="38" r="6" fill="#f0c9a3"/>
      <circle cx="78" cy="38" r="12" fill="#d39b6a" {s}/><circle cx="78" cy="38" r="6" fill="#f0c9a3"/>
      <ellipse cx="50" cy="62" rx="35" ry="31" fill="#d39b6a" {s}/>
      <ellipse cx="50" cy="74" rx="13" ry="9" fill="#f3dcc2"/>
      <ellipse cx="50" cy="69.5" rx="4" ry="3" fill="{INK}"/>'''
        return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">{body}' + face("#f29e9e").replace(
            '<path d="M44 70 q3 4 6 0 q3 4 6 0"', '<path d="M45 76 q2.5 3 5 0 q2.5 3 5 0"') + '</svg>'
    elif kind == "chick":
        body = f'''
      <path d="M48 22 q-6 -10 2 -12 q-1 6 4 4 q4 -2 3 6" fill="#f7d34f" {s}/>
      <ellipse cx="50" cy="60" rx="35" ry="33" fill="#fbe07a" {s}/>
      <path d="M17 66 q-8 4 -4 12 q8 -1 10 -8" fill="#f7d34f" {s}/>
      <path d="M83 66 q8 4 4 12 q-8 -1 -10 -8" fill="#f7d34f" {s}/>'''
        f = face("#f7a37b").replace('<path d="M44 70 q3 4 6 0 q3 4 6 0" fill="none"',
                                     '<path d="M44 68 L56 68 L50 75 Z" fill="#f39a3c" stroke-linejoin="round"')
        return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">{body}{f}</svg>'
    else:  # cat
        body = f'''
      <path d="M18 46 L22 14 L44 34 Z" fill="#f7c08a" {s}/><path d="M24 36 L25 22 L36 32 Z" fill="#f9d7d0"/>
      <path d="M82 46 L78 14 L56 34 Z" fill="#f7c08a" {s}/><path d="M76 36 L75 22 L64 32 Z" fill="#f9d7d0"/>
      <ellipse cx="50" cy="62" rx="36" ry="30" fill="#f7c08a" {s}/>
      <path d="M40 36 q2 6 0 10 M50 34 q2 6 0 11 M60 36 q2 6 0 10" stroke="#e39a5a" stroke-width="3" fill="none" stroke-linecap="round"/>
      <path d="M12 64 l13 2 M12 72 l13 -1 M88 64 l-13 2 M88 72 l-13 -1" stroke="{INK}" stroke-width="1.8" stroke-linecap="round"/>'''
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">{body}{face()}</svg>'

def hanamaru(size, color="#ef5b5b"):
    import math
    petals = []
    n = 12; R = 40
    pts = [(50 + R * math.cos(2 * math.pi * i / n), 50 + R * math.sin(2 * math.pi * i / n)) for i in range(n + 1)]
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join(f"A11 11 0 0 1 {x:.1f} {y:.1f}" for x, y in pts[1:])
    sp = []
    for k in range(0, 260):
        t = k / 260 * 2.6 * 2 * math.pi
        r = 29 - 18 * k / 260
        sp.append(f"{50 + r * math.cos(t - 1.6):.1f},{50 + r * math.sin(t - 1.6) * 0.92:.1f}")
    return (f'<svg viewBox="-4 -4 108 108" style="width:{size}mm;height:{size}mm">'
            f'<path d="{d}Z" fill="#fff" stroke="{color}" stroke-width="5" stroke-linejoin="round"/>'
            f'<polyline points="{" ".join(sp)}" fill="none" stroke="{color}" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def star(color, size, rot=0):
    return (f'<svg viewBox="0 0 24 24" style="width:{size}mm;height:{size}mm;transform:rotate({rot}deg)">'
            f'<path d="M12 2.5l2.8 6 6.5.7-4.9 4.4 1.4 6.4L12 16.8 6.2 20l1.4-6.4L2.7 9.2l6.5-.7z" '
            f'fill="{color}" stroke="#fff" stroke-width="1.2" stroke-linejoin="round"/></svg>')

def heart(color, size, rot=0):
    return (f'<svg viewBox="0 0 24 24" style="width:{size}mm;height:{size}mm;transform:rotate({rot}deg)">'
            f'<path d="M12 21s-8-5.2-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 5.8-8 11-8 11z" '
            f'fill="{color}" stroke="#fff" stroke-width="1.2"/></svg>')

