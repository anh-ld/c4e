# 1. download web apge
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com"
# open connection
html = urlopen(url)
# read and decode
html_content = html.read().decode('utf-8')
# save html web page to local storage
# html_file = open("dantri.html","w")
# html_file.write(html)
# html_file.close()
# 2. Extract ROI (Region of Interest)
soup = BeautifulSoup(html_content,"html.parser")
ul = soup.find("ul","ul1 ulnew")
# 3. Extract Info
li_list = ul.find_all("li")
l = []

for li in li_list:
    a = li.h4.a
    # print(a.string)
    # print(url + a["href"])
    # print("*" * 30)
    l.append({"title": a.string,"link":url + a["href"]})

pyexcel.save_as(records=l, dest_file_name="1.xls")
