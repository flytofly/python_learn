import urllib2
from sgmllib import SGMLParser
__author__ = 'Administrator'
class Spider(SGMLParser):
        def __init__(self):
                SGMLParser.__init__(self)
                self.is_a = ""
                self.name = []
        def start_li(self,attrs):
                self.is_a = 1
        def end_li(self):
                self.is_a = ""
        def handle_data(self, data):
                if self.is_a == 1:
                        self.name.append(data)

if __name__  == '__main__':
        fo = open("D:/sparkFile/sina_resu.txt", "wb")
        content = urllib2.urlopen('http://mil.news.sina.com.cn/').read()
        #content = open("D:/sparkFile/pyTest.txt",'r+').read()
        spi = Spider()
        spi.feed(content)
        for item in spi.name:
                        print item.decode('utf8').encode('gbk')
                        fo.write(item)
        fo.close()