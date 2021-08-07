"""
需求：百度翻译
-post请求：携带参数

"""
import requests
import json

# 1.指定rul
post_url = 'https://fanyi.baidu.com/sug'
# 2.进行UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
}
word = input('enter a word:')
# 3.post请求参数处理（同get请求一致）
data = {
    'kw': word
}
# 4.请求发送
response = requests.post(url=post_url, data=data, headers=headers)
# 获取响应数据，json（）方法返回的是obj
dic_obj = response.json()

# 持久化数据
filename=word+'.json'
fp = open('./'+filename, 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)
