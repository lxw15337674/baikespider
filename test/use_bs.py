from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print('获取所有的连接')
links = soup.find_all('a')
for link in links:
    print(link.name,link['href'],link.get_text())

print('获取tillie的链接')
link_node= soup.find('a',href="http://example.com/tillie" )
print(link.name, link['href'], link.get_text())

print('正则匹配')
links= soup.find_all('a',href=re.compile((r"ill")) )
for link in links:
    print(link.name,link['href'],link.get_text())

print('获取p段落文字')
p_node= soup.find('p',class_='title') #此处class是python关键字,所以要加_
print(p_node.name,p_node.get_text())