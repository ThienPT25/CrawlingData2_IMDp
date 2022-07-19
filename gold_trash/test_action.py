import requests, json
from bs4 import BeautifulSoup

def movies_page(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find_all("h3", class_="lister-item-header")
    for movie_link in titles:
        movies_links.append(movie_link.find("a").attrs["href"])
    return movies_links

def movie_page_next(link):
    next_ = []
    response = requests.get("https://www.imdb.com" + link)
    soup = BeautifulSoup(response.content, "html.parser")
    next_button = soup.find_all("div", class_="desc")
    for next_link in next_button:
        next_.append(next_link.find("a").attrs["href"])
    return next_

# # Lấy Url Genre từ file URLGenre.json
# json_file = open("./URLGenre.json", "r", encoding="utf-8")
# url_genre = json.load(json_file)
movies_links = []
next_links = []
next_links_page = []
links_101_9951 = []

# # Tìm link đến trang start = 9951
# url = "https://www.imdb.com/search/title/?title_type=feature&genres=action&start=51&explore=genres&ref_=adv_nxt"
# for i in range(51, 9951, 50):
#     url = url.replace(str(i), str(i + 50))
#     links_101_9951.append(url)

# Tìm link next_page bắt đầu từ trang start = 10051
# movie_page_next("/search/title/?title_type=feature&genres=crime,thriller&after=WzEwMTYwMDUsInR0NDE0NjYzMiIsMTAwNTFd&explore=genres&ref_=adv_nxt")
while len(next_links) != 0:
    next_links_page.append(next_links[0])
    movie_page_next(next_links[0])
    print(len(next_links_page))
print(next_links_page)

# # URL trang 1, 2 --> start = 9951, 10001, 10051 thể loại action
# links = [url_genre[0], url] + links_101_9951 + ["https://www.imdb.com/search/title/?title_type=feature&genres=action&after=Wzk4Nzc3LCJ0dDUzMDcyNjYiLDEwMDAxXQ%3D%3D&explore=genres&ref_=adv_nxt"]

# # Lấy links movie trang 1, 2 --> start = 9951, 10001, 10051
# for link in links:
#     movies_page(link)

