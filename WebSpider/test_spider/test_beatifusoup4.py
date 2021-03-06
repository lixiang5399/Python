#coding:utf8
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

print(u'获取所有连接')
links = soup.find_all('a')
for i in links:
    print i.name, i['href'], i.get_text();

print(u'只获取一个链接')
link1 = soup.find('a',href='http://example.com/tillie')
print link1.name, link1['href'], link1.get_text();

print(u'正则匹配')
link2 = soup.find('a', href=re.compile(r'''\w+\lie'''))
print link2.name, link2['href'], link2.get_text()