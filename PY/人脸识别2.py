 # encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=dflyZoR8kWaWXgXHRqEtrs3S&client_secret=grP0L6VYMhwnvV5soCRtB47N6mZ8ztzE'
response = requests.get(host)
result = response.json()
if response:
    print(response.json())
    print('\n')
    access_token = response.json()['access_token']
    print(access_token)
    # print('\n')
    # print(access_token)