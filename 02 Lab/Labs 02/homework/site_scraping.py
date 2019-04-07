from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content,"html.parser")
table_content = soup.find("table",id = "tableContent")

table = []
headings = ["","Quy 4 - 2016", "Quy 1 - 2017", "Quy 2 - 2017", "Quy 3 - 2017"]

tr_list = table_content.find_all("tr")
for tr in tr_list:
    data = {}
    td_list = tr.find_all("td","b_r_c")
    td_list = td_list[:5]
    for td in td_list:
        data[headings[td_list.index(td)]] = td.string
    table.append(data)

pyexcel.save_as(records=table, dest_file_name="site_scraping.xlsx")
