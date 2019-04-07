from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel
# Part 1
url = "https://www.apple.com/itunes/charts/songs/"
html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content,"html.parser")
section = soup.find("section","section chart-grid").div.ul
li_list = section.find_all("li")

table = []
for li in li_list:
    song = li.h3.a.string
    artist = li.h4.a.string
    table.append({"Songs": song, "Artists": artist})

pyexcel.save_as(records=table, dest_file_name="itunes_top_songs.xlsx")
# Part 2
options = {
    'default_search': 'ytsearch',
    'max_downloads': len(table)
}
dl = YoutubeDL(options)
for song in table:
    dl.download([song["Songs"]+song["Artists"]])
