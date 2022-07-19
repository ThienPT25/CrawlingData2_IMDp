from os import link
from re import A
from bs4 import BeautifulSoup
import requests
import json
import csv

# Lấy link từng bộ movie
def movies_page(link):
    response = requests.get("https://www.imdb.com" + link)
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find_all("h3", class_="lister-item-header")
    movies_links = [movie_link.find("a").attrs["href"] for movie_link in titles]
    return movies_links

# Lấy link next page sau
def movie_page_next(link):
    response = requests.get("https://www.imdb.com" + link)
    soup = BeautifulSoup(response.content, "html.parser")
    next_button = soup.find_all("div", class_="desc")
    next_links = [next_link.find("a").attrs["href"] for next_link in next_button]
    return next_links

# Lấy Url Genre từ file URLGenre.json
json_file = open("./URLGenre.json", "r", encoding="utf-8")
url_genre = json.load(json_file)

# # Truy cập vào link film trang 1 action và crawl
movies_pages = movies_page(url_genre[0])
# for href in movies_pages:
#     crawl(href)

# # Truy cập vào link film trang 2 action và crawl
movie_pages_next = movies_page(movie_page_next(url_genre[0])[0])
# for href in movie_pages_next:
#     crawl(href)
    
#Tìm link từ start = 101 đến trang start = 9951
for i in range(51, 9951, 50):
    movie_pages_next = movie_pages_next[0].replace(str(i), str(i + 50))
    list_page = [movie_pages_next]
    print(list_page)  
    # print(i) 
# for href in list_page:
#     for href in movies_page(href):
#         crawl(href)
    

# for i in range(1, 9901, 50):
#     link = next_hrefs.replace(str(i-50), str(i))
#     next_hrefs = list(map(lambda x : x.replace(str(i), str(i + 50)), next_hrefs))
#     list_page = ["https://www.imdb.com" + next_hrefs[0]]
# for href in list_page:
#     response = requests.get(href)
#     soup = BeautifulSoup(response.content, "html.parser")
#     titles = soup.find_all("h3", class_="lister-item-header")
#     movies_links = [movie_link.find("a").attrs["href"] for movie_link in titles]
#     movies_hrefs = list(movies_links)

# # Tìm nội dung movie từng bộ phim trang start = 101 - start = 9951
#     for href in movies_hrefs:
#         response = requests.get("https://www.imdb.com" + href)
#         soup = BeautifulSoup(response.content, "html.parser")
#         crawl()



# # Truy cập vào link film trang 1 action
# response = requests.get(url_genre[0])
# soup = BeautifulSoup(response.content, "html.parser")
# titles = soup.find_all("h3", class_="lister-item-header")
# movies_links = [movie_link.find("a").attrs["href"] for movie_link in titles]
# movies_hrefs = list(movies_links)

# #Tìm link vào trang 2
# next_button = soup.find_all("div", class_="desc")
# next_links = [next_link.find("a").attrs["href"] for next_link in next_button]
# next_hrefs = list(next_links)

# # Tìm nội dung movie từng bộ phim trang 1
# for href in movies_hrefs:
#     response = requests.get("https://www.imdb.com" + href)
#     soup = BeautifulSoup(response.content, "html.parser")
#     crawl()

# # Truy cập link phim trang 2
# response = requests.get("https://www.imdb.com" + next_hrefs[0])
# soup = BeautifulSoup(response.content, "html.parser")
# titles = soup.find_all("h3", class_="lister-item-header")
# movies_links = [movie_link.find("a").attrs["href"] for movie_link in titles]
# movies_hrefs = list(movies_links)

# # Tìm nội dung movie từng bộ phim trang 2
# for href in movies_hrefs:
#     response = requests.get("https://www.imdb.com" + href)
#     soup = BeautifulSoup(response.content, "html.parser")
#     crawl()

# #Tìm link đến trang start = 9951
# list_page = []
# for i in range(1, 9901, 50):
#     i = i + 50
#     next_hrefs = list(map(lambda x : x.replace(str(i), str(i + 50)), next_hrefs))
#     list_page.append("https://www.imdb.com" + next_hrefs[0])
# for href in list_page:
#     response = requests.get(href)
#     soup = BeautifulSoup(response.content, "html.parser")
#     titles = soup.find_all("h3", class_="lister-item-header")
#     movies_links = [movie_link.find("a").attrs["href"] for movie_link in titles]
#     movies_hrefs = list(movies_links)

# # Tìm nội dung movie từng bộ phim trang start = 101 - start = 9951
#     for href in movies_hrefs:
#         response = requests.get("https://www.imdb.com" + href)
#         soup = BeautifulSoup(response.content, "html.parser")
#         crawl()

# #Truy cập vào trang start = 10001
# response = requests.get("https://www.imdb.com/search/title/?title_type=feature&genres=action&after=Wzk4Nzc3LCJ0dDUzMDcyNjYiLDEwMDAxXQ%3D%3D&explore=genres&ref_=adv_nxt")
# soup = BeautifulSoup(response.content, "html.parser")
# titles = soup.find_all("h3", class_="lister-item-header")
# movies_links = [movie_link.find("a").attrs["href"] for movie_link in titles]
# movies_hrefs = list(movies_links)

# # Tìm nội dung movie từng bộ phim trang start = 10001
# for href in movies_hrefs:
#     response = requests.get("https://www.imdb.com" + href)
#     soup = BeautifulSoup(response.content, "html.parser")
#     crawl()

# #Truy cập vào trang start = 10051
# response = requests.get("https://www.imdb.com/search/title/?title_type=feature&genres=action&after=Wzk5MzA4LCJ0dDAzMzgyNTgiLDEwMDUxXQ%3D%3D&explore=genres&ref_=adv_nxt")
# soup = BeautifulSoup(response.content, "html.parser")
# titles = soup.find_all("h3", class_="lister-item-header")
# movies_links = [movie_link.find("a").attrs["href"] for movie_link in titles]
# movies_hrefs = list(movies_links)

# # Tìm nội dung movie từng bộ phim trang start = 10051
# for href in movies_hrefs:
#     response = requests.get("https://www.imdb.com" + href)
#     soup = BeautifulSoup(response.content, "html.parser")
#     crawl()

# #Tìm link vào trang sau
# next_button = soup.find_all("div", class_="desc")
# next_links = [next_link.find("a").attrs["href"] for next_link in next_button]
# next_hrefs = list(next_links)

# while len(next_hrefs[0]) != 0:
#     # Truy cập link phim trang sau
#     response = requests.get("https://www.imdb.com" + next_hrefs[0])
#     soup = BeautifulSoup(response.content, "html.parser")
#     titles = soup.find_all("h3", class_="lister-item-header")
#     movies_links = [movie_link.find("a").attrs["href"] for movie_link in titles]
#     movies_hrefs = list(movies_links)
    
#     # Tìm link vào trang sau
#     next_button = soup.find_all("div", class_="desc")
#     next_links = [next_link.find("a").attrs["href"] for next_link in next_button]
#     next_hrefs = list(next_links)
    
#     # Tìm nội dung movie từng bộ phim trang start = 10051
#     for href in movies_hrefs:
#         response = requests.get("https://www.imdb.com" + href)
#         soup = BeautifulSoup(response.content, "html.parser")
#         crawl()
        
# # # Mở file json để điền
# # json_files = open('CralingData.json', 'w', encoding="utf-8")

# # # Mở file csv để điền
# # csv_files = open('CralingData.csv', 'w', newline= "", encoding="utf-8")
# # csv_writer = csv.writer(csv_files)
# # csv_writer.writerow(["Title", "Genre", "TitleOriginal_year_rating_runtime", "IMDb_Rating", "popularity", "describe", "director_writters_stars", "userreview_criticreview_metascore"])

# # # In vào list thông tin movie
# # infor_movie = [title, "action", TitleOriginal_year_rating_runtime, IMDb_Rating, popularity, describe, director_writters_stars, userreview_criticreview_metascore]
# # # Điền vào file json
# # json.dump(infor_movie, json_files)
# # # Điền vào file csv
# # csv_writer.writerow([title, "action", TitleOriginal_year_rating_runtime, IMDb_Rating, popularity, describe, director_writters_stars, userreview_criticreview_metascore])  
# # # print(infor_movie)