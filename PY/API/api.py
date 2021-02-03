import base64
import requests
import json
import urllib
import sys
import ssl
import json
import base64
import cv2
global token
url = 'http://hn216.api.yesapi.cn/?s=App.Open_Baidu.LocationIP&return_data=0&app_key=5EB7C6FD54CF9CDD7A442F0FEC24AB04&sign=E70E38BAB6CFE7B9C9C2D3299BDD5135'
s = requests.session()
# node = (node=uuid.getnode())
# mac = str(uuid.UUID(int=node).hex[-12:])
res1 = s.get(url).text
print(type(res1))
res2 = json.loads(res1)['data']['ip']
print(type(res2))
# req = Request(url)
print(res1, '  22   22', res2)
# {"ret": 200, "data": {"err_code": 0, "err_msg": "正常", "address": "CN|湖北|武汉|None|UNICOM|0|0", "content": {"address_detail": {"province": "湖北省", "city": "武汉市", "district": "", "street": "",
# "street_number": "", "city_code": 218}, "address": "湖北省武汉市", "point": {"y": "3556525.7", "x": "12725759.65"}}, "ip": "113.57.237.26"}, "msg": "V3.3.0 YesApi App.Open_Baidu.LocationIP"}
