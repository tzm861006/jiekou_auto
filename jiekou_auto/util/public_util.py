import json
import re
from string import Template
def find(data):
    data = json.dumps(data)
    return re.findall("\\${(.*?)}",data)

def replace(data,dict):
    a = Template(data)
    return a.safe_substitute(dict)

def search(list,response):
    if not list:
        return str(response)
    else:
        excute_data = response.get(list[0])
        del list[0]
        return search(list,excute_data)

a ="/v1/cards?token=${token}"
dict = {}
l = replace(a,dict)
print(l)

