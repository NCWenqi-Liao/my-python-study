
# import requests
#
# r = requests.get("http://www.baidu.com")#发送requests请求(模拟发送网络请求)，请求方式是get
# r.encoding = 'utf-8'
# print(r)#得到相应——————>200或418
# #print(r.headers)#------》得到标头





'''
import requests
#构造headers请求头协议
headers = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
            }
#通过requests模拟发送请求
r = requests.get("https://www.douban.com",headers = headers)#关键字传参数

#添加headers参数可以更真实地模拟正常的浏览器请求，因为有的网站有反爬的。

print(r)
'''

# import requests
# params = input("请输入搜索的词条")
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
# url =  f'https://baike.baidu.com/item/{params}'#用了占位符
#
# response = requests.get(url,headers = headers)#发送请求
# response.encoding = 'utf-8'#将获取的内容转化为utf-8形式
# print(response.text)


# import requests
# ers = {'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
# params = {'wd' : '南昌'}
#
# # params是传递搜索参数的
# r = requests.get("https://www.baidu.com/s?",headers = ers,params = params)
# r.encoding = 'utf-8'
#print(r.text)#得到相应——————>200或418
#print(r.headers)#------》得到标头
'''
import requests
url = "https://ptlogin.4399.com/ptlogin/login.do?v=1"
data = {"sec": 1,
"password": "U2FsdGVkX1+hS9rTPLWeIgY60yaFX2F/bepPiMb+PP8=",
"username": '961466365',
'autoLogin': 'on'}
headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
r = requests.post(url,data = data,)
# post请求会对页面内容做出改变
r.encoding = 'utf-8'
print(r.text)
'''

import requests

url = 'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1705654830194&loginType=3&uuid=181111935.1705389458997435807999.1705389458.1705389459.1705652813.2&productId=10088104653247&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield='
headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
r = requests.get(url,headers = headers)
r.encoding = 'utf-8'
print(r.json())
for i in r.json():
    print(i)




