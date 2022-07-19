from cgitb import html
from bs4 import BeautifulSoup
from isort import find_imports_in_paths
from matplotlib.pyplot import title
import requests

with open("simple.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml")
    
#print(soup.prettify()) 
    # -- Làm đẹp file html

#title1 = soup.head.title.text 
    # -- Lấy phần head --> title () theo text
#print(title1)

#title2 = soup.div 
    # -- Phần body div phần đầu
#print(title2)

#article = soup.find("div", class_="article") 
    # -- Find theo div có class = "article"
#print(article)
#headline = article.h2.a.text 
    # -- Lấy theo --> h2 --> a theo text
#print(headline)
#sumary = article.p.text 
    # -- Lấy theo --> p theo text
#print(sumary)

for article in soup.find_all("div", class_="article"):
    headline = article.h2.a.text
    print(headline)
    sumary = article.p
    print(sumary)
    print()
