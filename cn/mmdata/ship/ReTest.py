#coding:utf-8
import requests
import re
from lxml import etree
__author__ = 'Administrator'

if __name__ == '__main__':

    print("start parse ...")
    data = []
    html_content = requests.get('http://www.360kan.com/m/haPkY0osd0r5UB.html').content.lower()
    doc = etree.HTML(html_content)
    all_div = doc.xpath('//div[@class="yingping-list-wrap"]')
    for row in all_div:
        #获取每一个影评，即影评的item
        all_div_item = row.xpath('.//div[@class="item"]')  # find_all('div', attrs={'class': 'item'})
        for r in all_div_item:
            value = {}
            # 获取影评的标题部分
            title = r.xpath('.//div[@class="g-clear title-wrap"][1]')
            value['title'] = title[0].xpath('./a/text()')[0]
            value['title_href'] = title[0].xpath('./a/@href')[0]
            score_text = title[0].xpath('./div/span/span/@style')[0]
            score_text = re.search(r'\d+', score_text).group()
            value['score'] = int(score_text) / 20
            # 时间
            value['time'] = title[0].xpath('./div/span[@class="time"]/text()')[0]
            # 多少人喜欢
            value['people'] = int(
                    re.search(r'\d+', title[0].xpath('./div[@class="num"]/span/text()')[0]).group())
            data.append(value)
    print(data)