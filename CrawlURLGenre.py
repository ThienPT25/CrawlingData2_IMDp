from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://www.imdb.com/feature/genre/?ref_=nv_ch_gr")
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all("div", class_="table-cell primary")
links = [link.find("a").attrs["href"] for link in titles]
hrefs = list(links)
n = 24
list_url = []
for i in range(n):
    list.append("https://www.imdb.com" + hrefs[i])
with open('URLGenre.json', 'w', encoding="utf-8") as json_file:
    json.dump(list_url, json_file)