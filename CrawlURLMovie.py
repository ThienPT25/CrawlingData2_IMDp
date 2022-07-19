import requests, json
from bs4 import BeautifulSoup

# Lấy link movie
def movies_page(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find_all("h3", class_="lister-item-header")
    for movie_link in titles:
        movies_links.append(movie_link.find("a").attrs["href"])
    return movies_links

# Lấy link movie chi tiết
def get_links_movie(url, number):
    # Tìm link đến trang start = 501
    links_101_501 = []
    url_change = url
    for i in range(51, 501, 50):
        url_change = url_change.replace(str(i), str(i + 50))
        links_101_501.append(url_change)

    # URL trang 1, 2 --> start = 101 --> 501
    links = [url_genre[number], url] + links_101_501
    for link in links:
        movies_page(link)
    return movies_links

# Lấy Url Genre từ file URLGenre.json
json_file = open("./URLGenre.json", "r", encoding="utf-8")
url_genre = json.load(json_file)
url_genre.remove(url_genre[20])

# Lấy Url Genre từ file URLGenre_page2.json
json_file = open("./URLGenre_page2.json", "r", encoding="utf-8")
url_genre_page2 = json.load(json_file)
url_genre_page2.remove(url_genre_page2[20])

# Khai báo list
movies_links = []
list_b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# Lấy URL movie từng thể loại
for a, b in zip(url_genre_page2, list_b):
    get_links_movie(a, b)
    
# In ra file json URLMovie
with open('URLMovie.json', 'w', encoding="utf-8") as json_file:
    json.dump(movies_links, json_file)