import pymysql
from config.setting import dbconfig
from util.logging_util import logger

class util_pymysql():
    def __init__(self):
        self.db = pymysql.connect(**dbconfig)
        self.curor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.curor.close()
        self.db.close()

    def search_all(self,sql):
        self.curor.execute(sql)
        return self.curor.fetchall()

    def search_one(self,sql):
        self.curor.execute(sql)
        return self.curor.fetchone()

    def excuted(self,sql):
        try:
            self.curor.execute(sql)
            self.db.commit()
        except:
            logger.error("执行失败，正在回滚")
            self.db.rollback()




pymysql_cn = util_pymysql()
# c = pymysql_cn.search_all("select * from test_case_list ")
# print(c)
# c = pymysql_cn.search_one("select * from test_config where web='停车厂' and key='url'")
# print(c)

