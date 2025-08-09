import fontforge
import math
import unicodedata

WEDGES = {
  "uniF102": "V head",
  "uniF103": "V",
  "uniF104": "V short",
  "uniF105": "H head",
  "uniF106": "H",
  "uniF107": "H short",
  "uniF108": "V long",
  "uniF109": "H long",
  "uniF10A": "V mid",
  "uniF10B": "H mid",
  "uniF10C": "ninda",
  "uniF10D": "diag head",
  "uniF10E": "hi",
  "uniF10F": "V overlong",
  "uniF111": "H overlong",
  "uniF112": "Winkelhaken",
  "uniF113": "Winkelhaken small",
}

font = fontforge.open("Nabuninuaihsus.sfd")
for glyph_name in font:
  if not glyph_name.startswith("u12"):
    continue
  if any (part == "uniF110" for part, transform, _ in font[glyph_name].references):
    continue
  cp = chr(int(glyph_name[1:], base=16))
  print(glyph_name, cp, unicodedata.name(cp))
  for part, transform, _ in font[glyph_name].references:
    a11, a12, a21, a22, x, y = transform
    det = a11 * a22 - a12 * a21
    scale = math.sqrt(det)
    rotation = math.atan2(a21, a11)
    name = WEDGES.get(part)
    if not name:
      try:
        cp = chr(int(part[1:], base=16))
        name = unicodedata.name(cp).removeprefix("CUNEIFORM ")
      except:
        pass
    print(f"""{name or "":20} {
            f"scaled {scale}" if scale != 1 else ""
          } {
            f"rotated {math.degrees(rotation)}°" if rotation else ""
          } at ({x}, {y})""")