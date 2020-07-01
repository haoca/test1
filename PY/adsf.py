from lxml import etree
import requests
from lxml.html import fromstring, tostring

url = 'http://sh.lianjia.com/ershoufang/pudong'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
resl = requests.get(url,headers=headers)
tree = etree.HTML(resl.text)
 
res = tree.xpath('//ul[@class="sellListContent"]//div[@class="info clear"]//div[@class="title"]//a')[0]
res1 = etree.tostring(tree)
res2 = HTMLParser().unescape(res1.decode('utf-8'))
 
#用“/text()”取出文本值
text = tree.xpath('//ul[@class="sellListContent"]//div[@class="info clear"]//div[@class="title"]//a/text()')[0]
 
#用“/@href'”取出href值
href = tree.xpath('//ul[@class="sellListContent"]//div[@class="info clear"]//div[@class="title"]//a/@href')[0]
 
print(res)
print('===============================')
print(res2)
print('===============================')
print(text)
print('===============================')
print(href)
