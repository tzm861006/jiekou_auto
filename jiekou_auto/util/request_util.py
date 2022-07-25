from util.logging_util import logger
import requests

class request_util:
    def sent(self,url,data,method):
        logger.debug("接口地址为"+f"{url}"+",格式为"+f"{type(url)}")
        logger.debug("需要传递的参数为"+f'{data}'+",格式为"+f"{type(data)}")
        logger.debug("请求方式为" + f'{method}'+",格式为"+f"{type(method)}")
        if method=="post":
            result = requests.request("post",url,json=data)
        if method == "put":
            result = requests.request("put",url,json=data)

        dict ={}
        try:
            dict["body"] = result.json()
        except:
            dict["body"] = result.text

        dict["status_code"] = result.status_code

        return dict



