#!/usr/bin/env python
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
'''
Description

run cmdline :
pip install diff
'''

import difflib

tex1="""tex1:
this is a test for difflib ,just try to get difference of the log
现在试试功能是否可行 好呀
goodtest
那么试试吧好人
hkjhk
hkjhk
"""
tex1_lines=tex1.splitlines()
tex2="""tex2:
this is a test for difflib ,just try to get difference of the log
现在试试功能是否可行
goodtast
2
那么试试吧
khjk
hkjhk
"""
tex2_lines=tex2.splitlines()
#---------原始对比方法----------
#d=difflib.Differ()
#diff=d.compare(tex1_lines,tex2_lines)
#print '\n'.join(list(diff))

#--------html对比方法----------

#字符串对比
di = difflib.Differ()
diff = di.compare(tex1_lines, tex2_lines)

print('\n'.join(list(diff)))
print(len(list(diff)))
#生成html打哪
d= difflib.HtmlDiff()
q=d.make_file(tex1_lines,tex2_lines)

with open('diff.html', 'w') as f:
    f.write(q)

# 输出相似度


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).ratio()
similar = string_similar('你好', '你好啊')
similar1 = string_similar('a', 'a')
similar2 = string_similar('a', 'abc')
similar3 = string_similar('ae', 'abcd')

print('相似度:', similar, similar1, similar2, similar3)
