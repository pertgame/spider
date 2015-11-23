# -*- coding:utf-8 -*-

import re

page = u'总共10页'
pattern = re.compile(u'.*?\u5171(.*?)\u9875',re.S)
result = re.search(pattern,page)
print result.group(1)