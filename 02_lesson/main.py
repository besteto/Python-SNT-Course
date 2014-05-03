#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Тестовая программа - передать в скрипт строку, напечатать ее, перевернув каждое из слов, но сохранив порядок знаков препинания
"""
python main.py "to be, or not to be: that is the question" 
> ot eb, ro ton ot eb: taht si eht noitseuq
"""



import sys

import check_param
import split
import reverse

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

#ourStr = ""sys.argv[1]""
ourStr = "to be, or not to be: that is the question"
checkStr(ourStr)
startIndex = 0
endIndex = 0
for endIndex in len(ourStr):
	endIndex = splitStr(ourStr, startIndex)
	ouStr[startIndex:endIndex] = reverseStr(ourStr[startIndex:endIndex])
	startIndex = endIndex

print ouStr