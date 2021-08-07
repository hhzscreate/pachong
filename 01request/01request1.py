# 需求：爬取搜狗首页页面数据
import requests

# 指定url
url = 'https://www.sogou.com/'
# 发起请求
# get方法会返回一个响应对象
response = requests.get(url=url)
# 获取响应数据,text返回的是字符串形式的响应数据
page_text = response.text
print(page_text)
# 持久化存储
with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(page_text)