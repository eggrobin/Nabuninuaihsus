import fontforge

with open("Nabuninuaihsus_coverage.txt",
          mode="w", encoding="utf8") as f:
  font = fontforge.open("Nabuninuaihsus.sfd")
  for glyph_name in font:
    if any (part == "uniF110" for part, transform, _ in font[glyph_name].references):
      continue
    if font[glyph_name].unicode == -1:
      continue
    print("%04X" % font[glyph_name].unicode, file=f)

with open("CuneiformNAOutline_coverage.txt",
          mode="w", encoding="utf8") as f:
  font = fontforge.open("C:/Users/robin/Downloads/CuneiformNA.ttf")
  for glyph_name in font:
    if font[glyph_name].unicode == -1:
      continue
    print("%04X" % font[glyph_name].unicode, file=f)
