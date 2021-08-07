import requests
import json
url = 'https://movie.douban.com/typerank'
# type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '60',#从库中第几个电影前取
    'limit': '20'#一次取出的个数
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
}
response=requests.get(url=url,params=param,headers=headers)
list_data=response.json()
fp=open('./douban.json','w',encoding='utf-8')
json.dumps(list_data,fp=fp,ensure_ascii=False)
