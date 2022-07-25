import json

import pytest
from util.logging_util import logger
from util.public_util import *
from config.setting import Dyamic


from util.pymysql_util import pymysql_cn
from util.request_util import request_util
from util.read_mysql import readmysql

dy = Dyamic()
read = readmysql()
class Test_case:

    @pytest.mark.parametrize("case",read.load_all_case("停车场"))
    def test_ceshi(self,case):
        url =read.load_config("carpark","url")+ case["url"]
        method = case["method"]
        body = eval(case["request_body"])
        self.change_cardno(body,case)
        relation = case["relation"]
        tt = self.correlation(url)
        response = request_util().sent(tt,body,method)
        self.set_correlation(relation,response)
        self.assert_error(response,case)





    def correlation(self,data):
        dict = {}
        if find(data):
            for i in find(data):
                get_data = getattr(Dyamic,str(i),None)
                dict.update({str(i):get_data})
        return replace(data,dict)


    def set_correlation(self,relation,respnse):
        if relation != None and respnse !=None:
            list_first = relation.split("=")
            name = list_first[0]
            finl_list = list_first[1].split(".")
            shuju = search(finl_list,respnse)
            print(f"{name}= {shuju}")
            setattr(Dyamic,name,shuju)

    def assert_error(self,response,case):
        is_pass =False
        try:
            assert response["body"]["error_code"] == case["expected_code"]
            logger.debug("正确")
            is_pass = True

        except:
            is_pass= False
            logger.error("错误")

        finally:
            logger.debug(f"同步用例{case['id']}结果")
            read.updatetest_result(case["id"],response,is_pass)
            assert is_pass

    def change_cardno(self,body,case):
        if case["id"] == 2:
            dict_new = {"type":"1"}
            dict_new["cardno"]=str(int(body["cardno"])+1)
            data1 = json.dumps(dict_new)
            pymysql_cn.excuted(f"UPDATE `test_case_list` SET `request_body`='{data1}' WHERE id='2'")

# UPDATE `test_case_list` SET `request_body`='{\"cardno\":\"719358\",\"type\":\"1\"}' WHERE (`id`='2')





if __name__ == "__main__":
    pytest.main(["-vs"])
