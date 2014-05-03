#!/usr/bin/env python
# -*- coding: utf-8 -*-
#разделение на лексемы : split(str) -> [str,str...], возвращает список слов в строке. Что такое слово? Какова стратегия разделения

import re

def splitStr(param):
    return re.split('(\W+)',param)