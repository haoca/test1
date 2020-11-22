import requests
import json

data = {

    "ac_id": "1",
    "action": "login",
    "ajax": "1",

    "password": r"{B}YTEzMzA3MDIzMTg2",
    "save_me": "1",

    "username": "301737",
}

# newCookie = {}
# newCookie['key1'] = 'value1'
# newCookie['key2]='value2'
# newCookie['key3'] = 'value3'
# s = requests.session()
response = requests.post(
    url=r"http://172.30.16.34/srun_portal_pc.php?ac_id=1&",
    headers={
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN",
        "Cache-Control": "no-cache",
        "Connection": "Keep-Alive",
        "Content-Length": "109",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": r"login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUy%252BTpeX6WFL8ryAHkNUIMIRg8fKaHI8f1CqUBByT11ck7D3sVZEYQ88AMlEwvMxx3HvMShfJB0D4Kc5OdM3Wug3NB5WkHD3C87eiKEs8zw%253D%253D; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUy%252BTpeX6WFL8ryAHkNUIMIRg8fKaHI8f1CqUBByT11ck7D3sVZEYQ88AMlEwvMxx3HvMShfJB0D4Kc5OdM3Wug3NB5WkHD3C87eiKEs8zw%253D%253D; NSC_tsvo_4l_TH=ffffffffaf160e3b45525d5f4f58455e445a4a423660",
        "Host": "172.30.16.34",
        "Referer": "http://172.30.16.34/srun_portal_pc.php?ac_id=1&",
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)",
    },
    data={


        "action": "logout",
        "ajax": "1",

        "password": "a13307023186",


        "username": "301737",
    },
    # 这里配置了代理，因为我的操作安装了fiddler，这个你们没有说一定要弄

)
