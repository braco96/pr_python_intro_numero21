# -*- coding: utf-8 -*-
import re
def sumar_cadena(s):
    if not s: return 0
    sep = ','
    if s.startswith('//'):
        sep, s = s[2], s[3:]
    total = 0
    for trozo in s.replace('\n', sep).split(sep):
        total += int(trozo or 0)
    return total

