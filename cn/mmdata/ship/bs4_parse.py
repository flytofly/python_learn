#coding:utf-8
import requests
import re
import bs4
from bs4 import BeautifulSoup
__author__ = 'Administrator'

def getresu():
    print("start bs4 parse...")
    all_value = []
    value = {}
    html_content = requests.get('http://www.360kan.com/m/haPkY0osd0r5UB.html').content.lower()
    soup = BeautifulSoup(html_content,'html.parser')
    all_div = soup.find_all('div',attrs={'class':'yingping-list-wrap'},limit=1)
    for row in all_div:
        all_div_item = row.find_all('div',attrs={'class':'item'})
        for r in all_div_item:
            title = r.find_all('div',attrs={'class':'g-clear title-wrap'})
            print title
            if title is not None and len(title) > 0:
                value['title'] = title[0].a.string
                value['title_href'] = title[0].a['href']
                value['score'] = title[0].div.span.span['style']
                value['time'] = title[0].find_all('span',attrs={'class':'time'})[0].string
                #re.search(r'\d+',"值")  将值转化成Int类型
                value['peo_num'] = re.search(r'\d+', title[0].find_all('div',attrs={'class':'num'})[0].span.string).group()
            all_value.append(value)
            value = {}

    return all_value

if __name__ == '__main__':
    resu = getresu()
    for re in resu:
        print(re['title'])
        print(re['title_href'])
        print(re['score'])
        print(re['time'])
        print(re['peo_num'])
        print('======================')