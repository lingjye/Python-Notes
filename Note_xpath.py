#!/usr/bin/env python 
# encoding: utf-8
# product.py
# product
# Created by txooo on 2018/11/19
# Copyright © 2018 txooo. All rights reserved.

'''
Description

Please run cmdline :
pip install lxml

'''


from lxml import html

page_source = '''
<div>
  <ul id="side-menu">
    <li class="active">
      <a href="http://www.baidu.com/ws/project1/index.html">
        <i>图标</i>
        电子账户
        <span>箭头</span>
      </a>
      <ul class="nav">
        <li>子菜单1</li>
        <li>子菜单2</li>
      </ul>
    </li>
  </ul>
  <a href="http://www.baidu.com/ws/project2/index.html">1</a>
  <a href="http://www.baidu.com/ws/project2/login.html">2</a>
  <a href="http://www.baidu.com/xm/project2/index.htm ">2</a>
</div>
'''

html_etree = html.etree.HTML(page_source)

# 查找所有含ws的a标签
xpath_regx_ws = 'contains(%s, "%s")' % ('@href', 'ws')

href_ws = html_etree.xpath('//a[%s]' % xpath_regx_ws)
print(href_ws)

for each in href_ws:
	print(each.xpath('@href'))


# 查找所有含ws或xm且含index.htm的标签
xpath_regx_ws_index = '(contains(%s, "%s") or contains(%s, "%s")) and (contains(%s, "%s"))' % ('@href', 'ws', '@href', 'xm', '@href', 'index.htm')
href_ws_index = html_etree.xpath('//a[%s]' % xpath_regx_ws_index)
print(href_ws_index)
for each in href_ws_index:
	print(each.xpath('@href')[0].strip())
