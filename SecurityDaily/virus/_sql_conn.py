# -*- coding:utf-8 -*-

import pymssql

class Sql_Conn(object):
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def get_Conn(self):
        conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = conn.cursor()
        if not cur:
            raise(NameError, u'数据库连接失败')
        return conn, cur

    def sql_Act(self, sql):
        conn, cur = self.get_Conn()
        cur.execute(sql)
        retlist = cur.fetchall()
        conn.commit()
        conn.close()
        return retlist