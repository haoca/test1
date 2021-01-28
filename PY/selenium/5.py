# coding = utf-8
from selenium import webdriver
# options.binary_location = r'C:\Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\MicrosoftEdge.exe'

# driver_url = r"C:\Users\haost\Desktop\temp\PY\selenium\msedgedriver.exe"
# C: \Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe
browser = webdriver.Edge()
# options = webdriver.
# driver = webdriver.Edge()
driver = browser
driver.get("https://baidu.com")
driver.quit()


# options.add_argument('--headless')

# options.binary_location = r'C:\Users\haost\AppData\Roaming\360se6\Application\360se.exe'
# driver = webdriver.Chrome(options=options)
# driver.get('http://118.178.247.67:8081/systLogonUser/login.do')  # 打首金网登录页面
# time.sleep(1)
