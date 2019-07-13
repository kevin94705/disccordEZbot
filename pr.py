import requests
from bs4 import BeautifulSoup 

r = requests.get("http://zw.idv.tw/bd/boss/") #將網頁資料GET下來

print(r.text)