
import requests
import json

url = 'http://hn216.api.yesapi.cn/?s=App.Common_Weather.LiveWeather&return_data=0&city=%E6%AD%A6%E6%B1%89&app_key=5EB7C6FD54CF9CDD7A442F0FEC24AB04&sign=319DECDD0D63B8E1CD3B8AABD7F2CC71'
s = requests.session()
# node = (node=uuid.getnode())
# mac = str(uuid.UUID(int=node).hex[-12:])
res1 = s.get(url).text
print(type(res1))
res2 = json.loads(res1)['data']['weather']
print(type(res2))
for i in res2:

    try:
        print('\n'+i+':'+res2[str(i)])
    except:
        pass
