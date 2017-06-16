#coding:utf-8
import requests
import re
import bs4
import mysql.connector
from bs4 import BeautifulSoup
__author__ = 'Administrator'

#[[][]] 单条数据插入
def getDb(sqlstr):
    con=mysql.connector.connect(host='127.0.0.1',user='root',passwd='root',db='py_db',port=3306)
    cursor_=con.cursor()
    cursor_.execute('insert into share_test (code_num,code_name,code_nn,code_detail) values (%s,%s,%s,%s)',sqlstr)
    con.commit()
    con.close()

#[[][]] 批量数据插入
def getDbs(sqlstr):
    con=mysql.connector.connect(host='127.0.0.1',user='root',passwd='root',db='py_db',port=3306)
    cursor_=con.cursor()
    cursor_.executemany('insert into share_test (code_num,code_name,code_nn,code_detail) values (%s,%s,%s,%s)',sqlstr)
    con.commit()
    con.close()


if __name__ == '__main__':
    value = ""
    sqlstr = ""
    sql_wkk = ()
    list = []
    list_span = []
    data = []
    data_con = open("C:/Users/Administrator/Desktop/2017/python_file/eastmoney.html","r").read().strip().replace("\n","").decode("gbk").encode("utf-8")
    soup = BeautifulSoup(data_con,"html.parser")
    trs = soup.find_all('tr')
    for ev_tr in trs:
        tds = ev_tr.find_all('td')
        if tds is not None and tds is not "":
            for ev_td in tds:
                print ev_td.text
                value += (ev_td.text).replace(" ",",")
            value = value[:-2]
            valArr = value.split(",")
            for i in range(0,(valArr.__len__()-12)):
                sqlstr += "'"+valArr[i]+"',"
                list.append(valArr[i])
            if valArr is not None and valArr.__len__() > 2:
                data = [valArr[0],valArr[1],valArr[2],valArr[3]]
                list_span.append(data)
            sqlstr = ""
            value = ""
    getDbs(list_span)
    list_span = []
