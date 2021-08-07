# 需求：爬取肯德基
import requests
import json
# 指定url
url = 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'
# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
word=input('城市')
data = {
    'cname': '',
    'pid': '',
    'keyword': word,
    'pageIndex': '1',
    'pageSize': '10'
}
param={
    'keyword':word
}
response=requests.post(url=url,headers=headers,data=data,params=param)
data_text=response.text

filename=word+'.json'
fp=open(filename,'w',encoding='utf-8')
json.dump(data_text,fp=fp,ensure_ascii=False)

