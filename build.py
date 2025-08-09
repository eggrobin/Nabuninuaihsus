import fontforge

font = fontforge.open("Nabuninuaihsus.sfd")

font.selection.all()
font.unlinkReferences()
font.removeOverlap()
for glyph_name in font:
  font[glyph_name].left_side_bearing = int(font[glyph_name].left_side_bearing + 60)
  font[glyph_name].right_side_bearing = int(font[glyph_name].right_side_bearing + 60)
font.ascent = 800
font.descent = 200
font.generate("Nabuninuaihsus.otf")