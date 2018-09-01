from urllib.request import urlopen
import requests,urllib,re
import urllib.request

from bs4 import BeautifulSoup
url='https://www.douyu.com/g_yz'

headers=('User-Agent',' Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
         ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
req=urllib.request.Request(url)
req.add_header('User-Agent',' Mozilla/5.0 (Windows NT 10.0; Win64; x64 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
data=urlopen(req).read()
html=data.decode('utf-8')
bsobj=BeautifulSoup(html,'lxml')
find_div=bsobj.find('div',id='live-list-content')
# print(find_div)
find_img=find_div.findAll('span',class_='imgbox')
# print(find_img[0])
imgs=[]
for each in find_img:
    pat='https://.*.jpg'
    try:
        img=re.compile(pat).search(str(each))
        # print(img.findall(str(each)))
        imgs.append(img[0])
    except TypeError as e:
        print(e)
# print(imgs)
j = 1
for each in imgs:
    try:
        path = 'c:/users/lenovo/desktop/abc/%s.jpg'%(j)

        urllib.request.urlretrieve(each,path)
        j+=1
    except NoneType as e:
        print(e)
print('done.....')