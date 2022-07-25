import json
from datetime import datetime

from util.pymysql_util import pymysql_cn


class readmysql:
    def load_all_case(self, web):
        return pymysql_cn.search_all(f"select * from test_case_list where web = '{web}' ")

    def load_isdel(self, web):
        run_list = [case for case in self.load_all_case(web) if case["isdel"] == 1]
        return run_list

    def load_config(self, web,key):
        result = pymysql_cn.search_one(f"SELECT * FROM `test_config` WHERE `key` = '{key}' AND `web` = '{web}'  ")
        return result["value"]

    def updatetest_result(self,case_id,response,reult):
        self.now_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        rows =pymysql_cn.excuted(f"insert into test_result_record(case_id,times,response,result) values ('{case_id}','{self.now_time}','{json.dumps(response)}','{reult}')")
        return rows

a =readmysql()
c =a.load_config("carpark",'url')
print(c)

