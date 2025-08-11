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

font = fontforge.open("Nabuninuaihsus.sfd")

for c in (0xF122, 0xF123, 0xF124, 0xF128, 0xF132, 0xF133, 0xF137):
  font.selection.none()
  font.selection.select(("unicode",), c)
  font.copy()
  font.selection.none()
  font.selection.select(("unicode",), c - 0x20)
  font.paste()
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
font.familyname = "Nabuninuaihsus Sans"
font.fontname = "NabuninuaihsusSans"
font.fullname = "Nabuninuaihsus Sans"
font.generate("Nabuninuaihsus Sans.otf")