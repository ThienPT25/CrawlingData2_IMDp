from logging import exception
from unittest import skip
from bs4 import BeautifulSoup
from hamcrest import none
from prometheus_client import Summary
import requests
from sqlalchemy import null, true
import csv

csv_file = open("simple.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Headline", "Sumary", "Video_link"])
for i in range(17):
    i = i + 1
    source = requests.get("https://coreyms.com/page/" + str(i)).text
    soup = BeautifulSoup(source, "lxml")
    #print(soup.prettify())
    for article in soup.find_all("article"):
        try:
            headline = article.h2.a.text
        except Exception as e:
            headline = None
        print(headline)
        try:
            sumary = article.find("div", class_="entry-content").p.text
        except Exception as e:
            sumary = None
        print(sumary)
        # a = len(article.find_all("iframe"))
        # print(a)
    # Cách lấy link youtube 1
        # if len(article.find_all("iframe")) != 0:
        #     vid_src = article.find("iframe", class_="youtube-player")["src"]
        #     #print(vid_src)
        #     vid_id = vid_src.split("/")[4]
        #     vid_id = vid_id.split("?")[0]
        #     # #print(vid_id)
        #     yt_link = "https://youtube.com/watch?v=" + vid_id
        #     print(yt_link)
        #     print()
    # Cách lấy link youtube 2
        try:
            vid_src = article.find("iframe", class_="youtube-player")["src"]
            #print(vid_src)
            vid_id = vid_src.split("/")[4]
            vid_id = vid_id.split("?")[0]
            # #print(vid_id)
            yt_link = f"https://youtube.com/watch?v={vid_id}"
        except Exception as e:
            yt_link = None
        print(yt_link)
        csv_writer.writerow([headline, sumary, yt_link])
    
    
csv_file.close()