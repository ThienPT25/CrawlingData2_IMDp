import requests, json, csv
from bs4 import BeautifulSoup

# Hàm dùng để crawl dữ liệu
def crawl(href):
    response = requests.get("https://www.imdb.com" + href)
    soup = BeautifulSoup(response.content, "html.parser")
    try:
        Name_EnName_Year_Rating_Runtime = soup.find("div", class_="sc-94726ce4-2 khmuXj").text
        IMDb_Rating = soup.find("div", class_="sc-7ab21ed2-0 fAePGh").text
        popularity = soup.find("div", class_="sc-edc76a2-1 gopMqI").text
        allgenre = soup.find("div", class_="ipc-chip-list__scroller").text
        describe = soup.find("span", class_="sc-16ede01-2 gXUyNh").text
        director_writters_stars = soup.find("div", class_="sc-fa02f843-0 fjLeDR").text
        userreview_criticreview_metascore = soup.find("ul", class_="ipc-inline-list sc-124be030-0 ddUaJu baseAlt").text
        movie_infor = [Name_EnName_Year_Rating_Runtime, IMDb_Rating, popularity, allgenre, describe, director_writters_stars, userreview_criticreview_metascore]
        csv_writter.writerow([Name_EnName_Year_Rating_Runtime, IMDb_Rating, popularity, allgenre, describe, director_writters_stars, userreview_criticreview_metascore])
    except:
        movie_infor = [None, None, None, None, None, None, None]
    return movie_infor

# Mở file json để lấy list
json_file = open("./URLMovie.json", "r", encoding="utf-8")
url_movie = json.load(json_file)
url_movie = list(dict.fromkeys(url_movie))

# Mở file csv để điền dữ liệu vào
csv_file = open("infor_movie.csv", "w", newline="", encoding="utf-8")
csv_writter = csv.writer(csv_file)
csv_writter.writerow(["Name_EnName_Year_Rating_Runtime", "IMDb_Rating", "popularity", "allgenre", "describe", "director_writters_stars", "userreview_criticreview_metascore"])

# Lấy infor từng bộ movie trong list
for link in url_movie:
    crawl(link)