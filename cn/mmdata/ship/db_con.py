#coding:utf-8
import mysql.connector
def getDb():
    con=mysql.connector.connect(host='127.0.0.1',user='root',passwd='root',db='py_db',port=3306)
    cursor_=con.cursor()
    cursor_.execute('insert into share (share_num,share_name) values (%s, %s)',['8888', 'wkk232323beijingfengggu'])
    cursor_.rowcount
    con.commit()
    con.close()
if __name__ == '__main__':
    getDb()
