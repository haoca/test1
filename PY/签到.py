import time
from selenium import webdriver
# import os

username = "18200715012" # 请替换成你的用户名
password = "123456Bb" # 请替换成你的密码
code = 121

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

options.binary_location = r'C:\Users\haost\AppData\Roaming\360se6\Application\360se.exe'
driver = webdriver.Chrome(options=options)
driver.get('http://118.178.247.67:8081/systLogonUser/login.do') # 打首金网登录页面
time.sleep(1)

#找到用户名输入框点击获取焦点并输入信息
driver.find_element_by_id('userName').click()
driver.find_element_by_id('userName').send_keys(username)
driver.find_element_by_id('isAgree').click()
#找到密码输入框点击获取焦点并输入信息
driver.find_element_by_id('pwd').click()
driver.find_element_by_id('pwd').send_keys(password)

# 找到图形验证码输入框点击获取焦点输入信息
driver.find_element_by_id('verifyCode').click()
driver.find_element_by_id('verifyCode').send_keys(code)

# 找到登录按钮点击
driver.find_element_by_id('login').click()
time.sleep(1)

# 找到签到点击完成签到
driver.find_element_by_class_name('signIn').click()
driver.find_element_by_class_name('new-charge').click()

# driver.close()

# 这些是网站中定位到的元素
# userName
# pwd
# verifyCode
# login