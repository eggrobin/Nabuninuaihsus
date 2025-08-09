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
font.os2_typoascent = 800
font.os2_typoascent_add = False
font.os2_typodescent = -200
font.os2_typodescent_add = False
font.os2_use_typo_metrics = True
# Still better to clip than to space lines for 𒀱…
font.os2_winascent = 900
font.os2_winascent_add = False
font.os2_windescent = 200
font.os2_windescent_add = False
font.generate("Nabuninuaihsus.otf")