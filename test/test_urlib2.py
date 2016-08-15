#coding: utf8
"""网页下载器urllib模块"""
from urllib import request
import http.cookiejar

url = 'http://www.baidu.com'

print('第一种方法')
response1 = request.urlopen(url)
print(response1.getcode())  #返回代码 200即为正常
print(len(response1.read())) #网页长度

print('第二种方法')
req = request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
response2 = request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))

print('第三种方法')
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(len(response3.read()))
print(cj)