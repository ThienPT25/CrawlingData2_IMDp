from time import process_time_ns
from bs4 import BeautifulSoup
from inflection import titleize
import requests
import json
# from selenium import webdriver
# from time import sleep

json_files = open('CralingData.json', 'w', encoding="utf-8")
infor_movie = {}

def crawl():
    try:
        title = soup.find("div", class_="sc-94726ce4-2 khmuXj").h1.text
    except Exception as e:
        title = None
    # try:
    #     title_original = soup.find("div", class_="sc-dae4a1bc-0 gwBsXc").text
    # except Exception as e:
    #     title_original = None
    # try:
    #     year = soup.find("span", class_="sc-8c396aa2-2 itZqyK").text
    # except Exception as e:
    #     year = None
    try:
        titleOriginal_year_rating_runtime = soup.find("div", class_="sc-94726ce4-3 eSKKHi").text # Lọc Rating và Runtime
    except Exception as e:
        titleOriginal_year_rating_runtime = None
    try:
        IMDb_Rating = soup.find("div", class_="sc-7ab21ed2-0 fAePGh").text
    except Exception as e:
        IMDb_Rating = None
    try:
        popularity = soup.find("div", class_="sc-edc76a2-0 bZeUlh").text
    except Exception as e:
        popularity = None
    try:
        describe = soup.find("span", class_="sc-16ede01-2 gXUyNh").text
    except Exception as e:
        describe = None  
    # try:
    #     director = soup.find("a", class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
    # except Exception as e:
    #     director = None  
    try:
        director_writters_stars = soup.find("div", class_="sc-fa02f843-0 fjLeDR").text
    except Exception as e:
        director_writters_stars = None  
    # try:
    #     userreview = soup.find("span", class_="three-Elements").text
    # except Exception as e:
    #     userreview = None  
    try:
        userreview_criticreview_metascore = soup.find("ul", class_="ipc-inline-list sc-124be030-0 ddUaJu baseAlt").text
    except Exception as e:
        userreview_criticreview_metascore = None
    infor_movie = [title, titleOriginal_year_rating_runtime, IMDb_Rating, popularity, describe, director_writters_stars, userreview_criticreview_metascore]
    print(infor_movie)
    json.dump(infor_movie, json_files)

# Lấy Url Genre từ file URLGenre.json
json_file = open("./URLGenre.json", "r", encoding="utf-8")
url_genre = json.load(json_file)

# Đưa đường dẫn đến địa chỉ movies thể loại action
# Truy cập vào link film trang 1
response = requests.get(url_genre[0])
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all("h3", class_="lister-item-header")
movies_links = [link.find("a").attrs["href"] for link in titles]
movies_hrefs = list(movies_links)
# print(movies_hrefs)

# Tìm nội dung movie từng bộ phim trang 1
for href in movies_hrefs:
    response = requests.get("https://www.imdb.com" + href)
    soup = BeautifulSoup(response.content, "html.parser")
    crawl()

#Tìm link vào trang 2
next_button = soup.find_all("div", class_="desc")
next_links = [link.find("a").attrs["href"] for link in next_button]
next_hrefs = list(next_links)

# Truy cập link phim trang 2
response = requests.get("https://www.imdb.com" + next_hrefs[0])
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all("h3", class_="lister-item-header")
movies_links = [link.find("a").attrs["href"] for link in titles]
movies_hrefs = list(movies_links)

# Tìm nội dung movie từng bộ phim trang 2
for href in movies_hrefs:
    response = requests.get("https://www.imdb.com" + href)
    soup = BeautifulSoup(response.content, "html.parser")
    crawl()

#Tìm link đến trang start = 9951
list_page = []
for i in range(1, 9901, 50):
    i = i + 50
    next_hrefs = list(map(lambda x : x.replace(str(i), str(i + 50)), next_hrefs))
    list_page.append("https://www.imdb.com" + next_hrefs[0])
for href in list_page:
    response = requests.get(href)
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find_all("h3", class_="lister-item-header")
    movies_links = [link.find("a").attrs["href"] for link in titles]
    movies_hrefs = list(movies_links)

# Tìm nội dung movie từng bộ phim trang start = 101 - start = 9951
    for href in movies_hrefs:
        response = requests.get("https://www.imdb.com" + href)
        soup = BeautifulSoup(response.content, "html.parser")
        crawl()

#Truy cập vào trang start = 10001
response = requests.get("https://www.imdb.com/search/title/?title_type=feature&genres=action&after=Wzk4Nzc3LCJ0dDUzMDcyNjYiLDEwMDAxXQ%3D%3D&explore=genres&ref_=adv_nxt")
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all("h3", class_="lister-item-header")
movies_links = [link.find("a").attrs["href"] for link in titles]
movies_hrefs = list(movies_links)

# Tìm nội dung movie từng bộ phim trang start = 10001
for href in movies_hrefs:
    response = requests.get("https://www.imdb.com" + href)
    soup = BeautifulSoup(response.content, "html.parser")
    crawl()

#Truy cập vào trang start = 10051
response = requests.get("https://www.imdb.com/search/title/?title_type=feature&genres=action&after=Wzk5MzA4LCJ0dDAzMzgyNTgiLDEwMDUxXQ%3D%3D&explore=genres&ref_=adv_nxt")
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all("h3", class_="lister-item-header")
movies_links = [link.find("a").attrs["href"] for link in titles]
movies_hrefs = list(movies_links)

# Tìm nội dung movie từng bộ phim trang start = 10051
for href in movies_hrefs:
    response = requests.get("https://www.imdb.com" + href)
    soup = BeautifulSoup(response.content, "html.parser")
    crawl()

#Tìm link vào trang sau
next_button = soup.find_all("div", class_="desc")
next_links = [link.find("a").attrs["href"] for link in next_button]
next_hrefs = list(next_links)

while len(next_hrefs[0]) != 0:
# Truy cập link phim trang sau
    response = requests.get("https://www.imdb.com" + next_hrefs[0])
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find_all("h3", class_="lister-item-header")
    movies_links = [link.find("a").attrs["href"] for link in titles]
    movies_hrefs = list(movies_links)
# Tìm nội dung movie từng bộ phim trang start = 10051
    for href in movies_hrefs:
        response = requests.get("https://www.imdb.com" + href)
        soup = BeautifulSoup(response.content, "html.parser")
        crawl()

    #Tìm link vào trang sau
    next_button = soup.find_all("div", class_="desc")
    next_links = [link.find("a").attrs["href"] for link in next_button]
    next_hrefs = list(next_links)
    





# #Truy cập thư viện slenium để thao tác trang
# #1. Khai báo biến browser
# browser = webdriver.Chrome(executable_path = "./chromedriver.exe")
# #2. Mở thử một trang web
# browser.get("https://www.imdb.com/search/title/?title_type=feature&genres=action&after=Wzk5MzA4LCJ0dDAzMzgyNTgiLDEwMDUxXQ%3D%3D&explore=genres&ref_=adv_nxt")


