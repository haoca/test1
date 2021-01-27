import requests


def isConnected():

    try:
        html = requests.get("http://www.baidu.com", timeout=2)
        html = str(html.content)
        flag = html.find('www.hao123.com')
        # print(html, flag, '\n1')
        if flag >= 0:
            return 1
        else:
            return 0
    except:
        return False


if(isConnected()):
    print('123')
else:
    print('456')
