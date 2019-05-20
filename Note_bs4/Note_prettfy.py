#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.
'''
格式化html
'''

from bs4 import BeautifulSoup
import re

html_markup = '''<p class=”ecopyramid”>
<ul id=”producers”>
<li class=”producerlist”>
<div class=”name”>plants</div>
<div class=”number”>100000</div>
</li>
<li class=”producerlist”>
<div class=”name”>algae</div>
Output in Beautiful Soup
<div class=”number”>100000</div>
</li>
</ul>'''
soup = BeautifulSoup(html_markup,'html.parser')
print(soup.prettify())
reg1 = re.compile("<[^>]*>")
content = reg1.sub('',soup.prettify())
print(content)
l = [x.strip(' ') for x in content.split('\n') if x.strip(' ') != '']
print('\n'.join(l))
print(l)