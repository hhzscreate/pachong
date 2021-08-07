"""
需求：爬取化妆品生产许可证相关数据
-动态加载数据
-首页
"""
import requests

# 指定药监局url
url_ids = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
data = {
    'on': ' true',
    'page': ' 1',
    'pageSize': ' 15',
    'productName': '',
    'conditionType': ' 1',
    'applyname': '',
    'applysn': '',
}
headers = {
    'User-Agent': ' Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Mobile Safari/537.36',
}
# 获取链接
dic_ids = requests.post(url=url_ids, data=data).json()
# 具体链接信息存储
list_ids = []
#
list_json=[]
url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for dic in dic_ids[list]:
    dic['ID']

