#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Тестовая программа - передать в скрипт строку, напечатать ее, перевернув каждое из слов, но сохранив порядок знаков препинания
"""
python main.py "to be, or not to be: that is the question" 
> ot eb, ro ton ot eb: taht si eht noitseuq
"""

import sys
import re
from check_param import checkStr 

if len(sys.argv) == 2:
	ourStr = sys.argv[1]

	if checkStr(ourStr):
		ourStr = ''.join(w[::-1] for w in re.split('(\W+?)',ourStr))
		print ourStr

	else:
		print "Not a string"
else:
	print "invalid argument number"