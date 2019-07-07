import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.blackdesert.com.tw/News/Notice?boardType=2") #將網頁資料GET下來
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
sel = soup.select("div.td a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
for i in sel:
    print(i.text.strip())
    