#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
"""
python main.py "to be, or not to be: that is the question" 
> ot eb, ro ton ot eb: taht si eht noitseuq
"""

import sys
import re
from check_param import checkStr 

if len(sys.argv) >= 2 and checkStr(sys.argv[1]):
	ourStr = sys.argv[1]
	ourStr = ''.join(w[::-1] for w in re.split('(\W+?)',ourStr))
	print ourStr

else:
	print "invalid commandline"

# Что будет, если позвать программу с русским текстом? Почему? Как исправить?
# 
# Оценки : 
# 3 за реализацию (оно не работает на русских строках)
# 5 за инициативу - регэксп справляется лучше в данном случае
# Итоговая 4. Программа решает только поставленную (и бессмысленную) задачу, просто
# расширить до чего-то полезного - не выйдет.
#
#
#