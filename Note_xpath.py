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


""" 示例一
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
"""

""" 示例二
html_str = '''
<div class="sort_nr">
				<div class="sort_cont1"> <img src="http://www.78.cn/imgs/2018-11-22/201811221824235892591.jpg"></div><div class="sort_cont3">累计时间：个月<br> 信誉积分：分<em></em></div><div class="sort_cont4">投资：￥<strong>3-5万</strong></div><div class="sort_cont5"><span class="fl">仅剩名额<font color="#ec384b"><i id="num_js">18</i></font>个</span><p><em style="width: 84%;"></em></p></div>
				<script src="http://msg78.tbkf.net/pc/xxpf_phone.php?gid=8695"></script><div class="sort_cont6">
<ul style="margin-top: 0px;">
<li>广东梅州　1376666****<br>
正在与该项目进行<span class="axzx">在线咨询</span></li><li>宁波北伦　1820812****<br>
正在与该项目进行<span class="mfth">免费通话</span></li><li>河北唐山　1599490****<br>
正在与该项目进行<span class="mfth">免费通话</span></li><li>河北保定　1363514****<br>
正在与该项目进行<span class="mfth">免费通话</span></li><li>山西大同　1323821****<br>
正在与该项目进行<span class="axzx">在线咨询</span></li><li>北京昌平　1377117****<br>
正在与该项目进行<span class="mfth">免费通话</span></li><li>上海松江　1363514****<br>
正在与该项目进行<span class="axzx">在线咨询</span></li><li>天津和平　1523899****<br>
正在与该项目进行<span class="mfth">免费通话</span></li><li>安徽淮北　1396787****<br>
正在与该项目进行<span class="mfth">免费通话</span></li><li>安徽铜陵　1361454****<br>
正在与该项目进行<span class="mfth">免费通话</span></li></ul>
</div>
<div class="sort_cont11"><a href="http://gb.78.cn/huodong/hongbao/showHongbao.php?gid=8695&amp;hongbao_type=1&amp;hongbao=700&amp;is_ggy=1&amp;sid=61" class="_thickbox"><span><i>￥</i>700</span></a></div>
<div class="sort_cont9"><a data-tbchatlink="true" href="http://qudao.tbkf.net/TongBao/chatadp.php?adp=pc&amp;channel_id=31604&amp;proj_id=40056&amp;plat_id=1&amp;ids=31604&amp;vpage=http%253A%252F%252Fwww.78.cn%252Fweb%252Fzhajixingqiu%252Findex.htm&amp;adp_ver=2&amp;chat_ver=2.0&amp;extra_data=custom_id=8695&amp;user_id=0&amp;basekw=&amp;uckloadid=80F5nB.4a030e4&amp;tkid=80F5nB.XKHYvF&amp;isweb=1&amp;pinit=1556263179&amp;rpage=&amp;sid=61" target="_blank"></a></div>

                <div class="sort_cont10"><span>区域：</span>北京市<br>
                    <span>名称：</span>北京快道网络有限公司</div>
            </div>
'''

xpath_str = '//div[@class="sort_cont10"]'
etree_item = html.etree.HTML(html_str)

res = etree_item.xpath(xpath_str)
print(res)
for each in res:
	res_arr = each.xpath('text()')

for earh in res_arr:
	print(earh, type(earh))

print(res_arr, res_arr[0], res_arr[-1])
"""

""" 示例三
html_str = '''
<div class="header-bot laout  clearfix zoom">
        <ul>
            <li class="bot-li1"><img src="/images/icon1.jpg"> 品牌名称：<span>乐堂口手工拉茶茶饮</span></li>
            <li><img src="/images/icon2.jpg"> 投资额度：<span>5-10万</span></li>
            <li><img src="/images/icon3.jpg"> 招商对象：创业者</li>
            <li class=" bot-li8"><img src="/images/icon4.jpg"> 证件资质：三证齐全</li>
            <li class="bot-li1"><img src="/images/icon5.jpg"> 品牌发源地：上海市</li>
            <li><img src="/images/icon6.jpg"> 所属行业：餐饮娱乐</li>
            <li><img src="/images/icon7.jpg"> 经营模式：全国连锁</li>
            <li class=" bot-li8"><img src="/images/icon8.jpg"> 公司名称：上海少权餐饮企业管理有限公司</li>
        </ul>
		<div>
			<a href="#igbook" class="input bot-liuyan">给我留言</a>
			<a href="#igbook" class="bot-zixun input">免费咨询</a>
        </div>
    </div>
'''

xpath_str = '//div[@class="header-bot laout  clearfix zoom"]/ul'
xpath_str_1 = 'li[@class="bot-li1"]/text()'
xpath_str_2 = 'li[@class=" bot-li8"]/text()'

etree_item = html.etree.HTML(html_str)

res = etree_item.xpath(xpath_str)[0]
print(res)

res1 = res.xpath(xpath_str_1)[-1]
res2 = res.xpath(xpath_str_2)[-1]
print(res1, type(res1), str(res1).strip())

res1 = str(res1).split('：')
print(res1)
print(res2)
"""


html_str = """
<ul style="width: 873px;"> 
				   <li class="xmxq_SPX_img">
						<img src="https://static.2958.cn/mypic/2017-03/20170315102702.gif" width="96" height="58" alt="食里留香小吃车">
				   </li> 
				   <li class="xmxq_SPX_tit"> 
						<h1>食里留香小吃车</h1> 
						<span class="xmxq_show-pro-but">
							<a href="javascript:void(0);" class="show-pro-but-gbok S-click-gok">给我留言</a> 
							<a href="#igbook" class="show-pro-but-tel S-click-tel">免费咨询</a> 
						</span>
					</li> 
				    <li class="xmxq_SPX_xmbq"> 
						<span>
							<i>所属行业：</i>
							<a href="javascript:;" target="_blank">餐饮娱乐</a>
						</span> 
						<span>
							<i>投资金额：</i>
							<a href="javascript:;" class="red" target="_blank">1-3万</a>
						</span> 
					</li> 
					<li class="xmxq_SPX_xmbq"> 
						<span>
							<i>所在区域：</i>
							<a href="javascript:;" target="_blank">丰台区</a>
						</span>
						<span>
							<i>在线咨询：</i>
							<a href="javascript:;" target="_blank">108人</a>
						</span> 
					</li> 
					<li class="xmxq_SPX_xmbq"> 
						<span>
							<i>创业类型：</i>
							<a href="javascript:;" target="_blank">加盟开店</a>
						</span> 
						<span>
							<i>消费人群：</i>
							<a href="javascript:;" target="_blank">白领工人</a>*
							<a href="javascript:;" target="_blank">成人</a>
						</span>
					</li> 
				</ul>
"""

xpath_str = '//ul'
xpath_str_1 = 'li[@class="xmxq_SPX_xmbq"][position()=2]/span/a/text()'


etree_item = html.etree.HTML(html_str)

res = etree_item.xpath(xpath_str)[0]
print(res)

res1 = res.xpath(xpath_str_1)
print(res1, type(res1))
#
# res1 = str(res1).split('：')
# print(res1)
# print(res2)
