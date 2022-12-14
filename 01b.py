#!/usr/bin/env python3

import re

GIVEN = """
ENTREES, IJSSTUK, KLIEDER, RITSELT, SYSTEEM, STEKKIE, TERMINI
""".strip()

words = re.split(',\s*', GIVEN)
for w in [5,2,0,3,4,6,None,1]:
    if w is not None: print(words[w])
    else: print('M..I..S') # MERITES ? Why?
