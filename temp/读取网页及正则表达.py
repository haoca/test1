import urllib
# 在python3.3里面，用urllib.request代替urllib2
import urllib.request
import re
url = input('please input website:')
page = urllib.request.urlopen(url)
html = page.read()
print(type(html))
picFile = open('1.html', "wb")
picFile.write(html)
htmls = html.decode('utf-8')
ac = open('2.html', 'wb')
print(type(htmls))
reg = r'\b，.+?，bilibili\b'
impress = re.compile(reg)
content = re.findall(impress, htmls)

for i in content:
    print(i)
# ac.write(htmls)
