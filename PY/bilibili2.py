from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

options.binary_location = r'C:\Users\haost\AppData\Roaming\360se6\Application\360se.exe'
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(r'D:\chromedriver.exe', options=options)
# driver.get('https://www.baidu.com')
# print(driver.page_source)
# sleep(10)
# driver.quit()
try:
    driver.get("https://www.bilibili.com/")
    # driver.find_element_by_id('kw').send_keys('12306')
    #截图
    sleep(3)
    driver.get_screenshot_as_file("D:\\baidu12306.png")
except RuntimeError as error:
    print(error)
finally:
    driver.quit()