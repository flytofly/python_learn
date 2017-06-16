import requests
import re
import bs4
__author__ = 'Administrator'


if __name__ == '__main__':

    base_url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    html_content = requests.get('http://www.360kan.com/m/haPkY0osd0r5UB.html').content
    print html_content

