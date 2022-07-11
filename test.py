from bs4 import BeautifulSoup
from matplotlib.pyplot import title
import requests
import json

# response = requests.get("https://www.imdb.com/search/title/?title_type=feature&genres=action&start=51&explore=genres&ref_=adv_nxt")
# soup = BeautifulSoup(response.content, "html.parser")
# titles = soup.find_all("div", class_="desc")
# links = [link.find("a").attrs["href"] for link in titles]
# links = list(links)
# print(links)
# l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']
  
# # replace Pant with Ishan
# l = list(map(lambda x: x.replace('nt', 'Ishan'), l))
  
# # print list
# print(l)

i = 5
while i < 1000:
    i = i + 1
    print(i)




