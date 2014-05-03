#!/usr/bin/env python
# -*- coding: utf-8 -*-
#проверка параметра на тип строки : check(param) -> boolean, возвращает true, если param - строка и false в другом случае

import string

def checkStr(param):
	return isinstance(param, basestring)