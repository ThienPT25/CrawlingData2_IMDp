from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#1. Khai báo biến browser
browser = webdriver.Chrome(executable_path = "./chromedriver.exe")

#2. Mở thử một trang web
browser.get("https://facebook.com")

#2a. Điền thông tin user vào ô tài khoản và pass
txtUser = browser.find_element_by_id("email")
txtUser.send_keys("ptthiencoin1221x5@gmail.com") #Điền tài khoản

txtPass = browser.find_element_by_id("pass") 
txtPass.send_keys("passfake123") #Điền mật khẩu

#2b. Submit form
txtPass.send_keys(Keys.ENTER)

#3. Dừng chương trình 5s
sleep(20)

#4. Đóng trình duyệt
browser.close()

