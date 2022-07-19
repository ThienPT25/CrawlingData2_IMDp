import pandas as pd
from icrawler.builtin import GoogleImageCrawler
from icrawler import ImageDownloader
from PIL import Image
from six import BytesIO

peoples_df = pd.read_csv('./dim_product.csv') #Lấy ra bảng CSV
# print(peoples_df) 
# print(peoples_df[['name', 'sku']]) #Lấy ra 2 cột
for row in peoples_df['name']:
    drow = row.replace("REPLAY", "")
    drow1 = drow.replace(",", "")
    drow2 = drow1.replace("  ", " ")
    drow3 = drow2.strip()
    lists = [drow3]
    for i in lists:
        google_Crawler = GoogleImageCrawler(storage = {'root_dir': i})
        google_Crawler.crawl(keyword = i, max_num = 1)
        