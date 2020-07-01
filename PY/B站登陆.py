import time
from selenium import webdriver
# import os
def cookie_to_dict(cookie):
    cookie_dict = {}
    items = cookie.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        cookie_dict[key] = value
    return cookie_dict


username = "18200715012" # 请替换成你的用户名
password = "123456Bb" # 请替换成你的密码
code = 121

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
cookies = {'value': 'LIVE_BUVID=AUTO9615869423079259; _uuid=25C984FD-6E8C-D245-B054-B337DCCA655F13114infoc; buvid3=6FD6DDC7-E508-4282-B204-0CF96FB58C7753931infoc; UM_distinctid=1717d4520a168-0c84987654fcc5-376b4502-e1000-1717d4520a235b; sid=9gkohsod; CURRENT_FNVAL=16; rpdid=|(u)Y~Ju)l|k0J\'ul)Ymlulm~; DedeUserID=169284469; DedeUserID__ckMd5=4c5234f4400d0738; SESSDATA=045ddd00%2C1602927157%2C16e62*41; bili_jct=70083ae6cd047d0edbcc1e29c0813882; CURRENT_QUALITY=120; bp_video_offset_169284469=405867816701256512; bp_t_offset_169284469=405919214576249055; _dfcaptcha=092af0924784a7d5f4a4f5944736b055; PVID=3','name': 'ketangpai_home_remember'}
# cookies ='LIVE_BUVID=AUTO9615869423079259; _uuid=25C984FD-6E8C-D245-B054-B337DCCA655F13114infoc; buvid3=6FD6DDC7-E508-4282-B204-0CF96FB58C7753931infoc; UM_distinctid=1717d4520a168-0c84987654fcc5-376b4502-e1000-1717d4520a235b; sid=9gkohsod; CURRENT_FNVAL=16; rpdid=|(u)Y~Ju)l|k0J\'ul)Ymlulm~; DedeUserID=169284469; DedeUserID__ckMd5=4c5234f4400d0738; SESSDATA=045ddd00%2C1602927157%2C16e62*41; bili_jct=70083ae6cd047d0edbcc1e29c0813882; CURRENT_QUALITY=120; bp_video_offset_169284469=405867816701256512; bp_t_offset_169284469=405919214576249055; _dfcaptcha=092af0924784a7d5f4a4f5944736b055; PVID=3'
options.binary_location = r'C:\Users\haost\AppData\Roaming\360se6\Application\360se.exe'
driver = webdriver.Chrome(options=options)
driver.get('https://link.bilibili.com/p/center/index#/user-center/my-info/operation') # 打首金网登录页面
driver.add_cookie(cookie_dict=cookies)
time.sleep(1)
driver.get('https://link.bilibili.com/p/center/index#/user-center/my-info/operation') # 打首金网登录页面


#找到用户名输入框点击获取焦点并输入信息
# driver.find_element_by_id('login-username').click()
# driver.find_element_by_id('login-username').send_keys(username)

# driver.find_element_by_id('login-passwd').click()
# driver.find_element_by_id('login-passwd').send_keys(password)

# #找到密码输入框点击获取焦点并输入信息
# driver.find_element_by_id('pwd').click()
# driver.find_element_by_id('pwd').send_keys(password)

# # 找到图形验证码输入框点击获取焦点输入信息
# driver.find_element_by_id('verifyCode').click()
# driver.find_element_by_id('verifyCode').send_keys(code)

# # 找到登录按钮点击
# driver.find_element_by_id('login').click()
# time.sleep(1)

# # 找到签到点击完成签到
driver.find_element_by_class_name('btn-login:hover').click()
driver.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/div[3]/div/div/div/div[5]/a[1]').click()
# driver.close()
time.sleep(1)

# 这些是网站中定位到的元素
# userName
# pwd
# verifyCode
# login