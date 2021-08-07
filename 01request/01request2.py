import requests

# 需求: 搜狐信息采集器
# UA伪造
# UA:User-Agent(请求载体的身份表示)
# UA检测：门户网站的服务器会检测对应的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器
# 检测到载体的身份标识不是基于某一款浏览器的，则表示为不正常请求
# 为不正常请求（爬虫），则服务端很有可能拒绝该次请求

# UA伪造：让爬虫对应的请求载体伪造成某款浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
}
url = 'https://www.sogou.com/web'
# 处理url携带的参数：封装到字典中
kw = input('enter a word:')
param = {
    'query': kw
}
# 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
response = requests.get(url=url, params=param, headers=headers)
page_text = response.text
filename = kw + '.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
