import requests


def insert_point():
    print('123')
    headers = {
        'authority': 'api.bilibili.com',
        'method': 'GET',
        'path': r'/x/v2/reply?callback = jQuery17203082160550519386_1612690453292 & jsonp = jsonp & pn = 1 & type = 1 & oid = 586523974 & sort = 2 & _ = 1612690717678',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN, zh;q = 0.9',
        'cookie': r'''_uuid = 6F10BC84-AD3C-5CB2-E838-916A2CA785C385693infoc; buvid3 = 972B21EC-9147-497A-9954-9AA29D231F95138401infoc; sid = 672as8af; DedeUserID = 169284469; DedeUserID__ckMd5 = 4c5234f4400d0738; SESSDATA = ff831e96 % 2C1613283905 % 2C03473*81; bili_jct = 355f6b2dad07e02ebd06f5bf6d75a4b7; rpdid = |(u)Y~Ju)Yu | 0J'ulm~~Jumk |; LIVE_BUVID=AUTO3915977344322780; LIVE_PLAYER_TYPE=1; CURRENT_QUALITY=120; blackside_state=0; CURRENT_FNVAL=80; buvid_fp_plain=972B21EC-9147-497A-9954-9AA29D231F95138401infoc; buivd_fp=972B21EC-9147-497A-9954-9AA29D231F95138401infoc; fingerprint3=3b54ea5c7b1727e06390f9b61b8367c1; fingerprint=b96121336af0a9015f2e0af0a165dd22; fingerprint_s=0cdf3884c98e688ad6630b1055703150; PVID=2; bp_video_offset_169284469=488986871378857356; bp_t_offset_169284469=488986871378857356; bfe_id=6f285c892d9d3c1f8f020adad8bed553''',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'dnt': '1',
        'referer': 'https: // www.bilibili.com/video/BV1Tz4y1U7oJ',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site'
    }
    date = {

    }
    url = 'https://www.bilibili.com/video/BV1Tz4y1U7oJ'
    rev = requests.get(url=url, headers=headers)
    print(rev)
    # print(rev)
    jsontxt = rev.text
    print(jsontxt)

    # text. (jsontxt)
    # title = jsonpath.jsonpath(jsontxt, '$..title')[0]
    # anthor = jsonpath.jsonpath(jsontxt, '$..author')[0]
    # url = jsonpath.jsonpath(jsontxt, '$..url')[0]
    # print(title, url)
insert_point()
