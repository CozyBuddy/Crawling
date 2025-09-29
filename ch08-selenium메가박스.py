from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl
import os
import urllib.request as req
opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach' , True)

opt.add_argument(r"--user-data-dir=C:\selenium\ChromeProfile")  # 원하는 경로
opt.add_argument(r'--profile-directory=Default')  # 기본 프로필

if not os.path.exists('./GOOGLE'):
    os.mkdir('./GOOGLE')
browser = webdriver.Chrome(options=opt)
browser.get('https://www.google.com/search?q=%EC%B9%B4%EB%A6%AC%EB%82%98+%EB%A0%88%EC%A0%84%EB%93%9C&sca_esv=0d6ac296c3e410be&udm=2&biw=1912&bih=924&sxsrf=AE3TifPEaRc1SWBH0ZJ_HVg3vMuZyj9gUw%3A1758420789188&ei=NV_PaMmhC7nGvr0PvfSG6AU&ved=0ahUKEwiJkIX04-iPAxU5o68BHT26AV0Q4dUDCBE&uact=5&oq=%EC%B9%B4%EB%A6%AC%EB%82%98+%EB%A0%88%EC%A0%84%EB%93%9C&gs_lp=Egtnd3Mtd2l6LWltZyIT7Lm066as64KYIOugiOyghOuTnDIIEAAYgAQYsQMyBhAAGAcYHjIGEAAYBxgeMgUQABiABDIFEAAYgAQyBhAAGAcYHjIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI8whQsQJYsQJwAXgAkAEAmAGEAaABhAGqAQMwLjG4AQPIAQD4AQGYAgKgAokBmAMAiAYBkgcDMS4xoAfDBbIHAzAuMbgHiAHCBwUwLjEuMcgHBA&sclient=gws-wiz-img')

# id = browser.find_element(By.CSS_SELECTOR , 'input#loginId--1')
# id.send_keys('kwonsunny@naver.com')

# pw = browser.find_element(By.CSS_SELECTOR , 'input#password--2')
# pw.send_keys('k011022k')
# button = browser.find_element(By.CSS_SELECTOR ,'button.btn_g.highlight.submit')

# button.click()
time.sleep(5)

imgs = browser.find_elements(By.CSS_SELECTOR , 'div.H8Rx8c img')
title = browser.find_elements(By.CSS_SELECTOR , 'div.toI8Rb.OSrXXb')
import re
print(title)
num = 0 
for x,y in zip(imgs,title):
    print(x.get_attribute('src'))
    print(f'제목 :{y.text}')

    # safe_title = re.sub(r'[\\/*?:"<>|]', "", y.text).strip()
    safe_title = y.text.strip().replace("\\","").replace("/","").replace("*","").replace("?","").replace(":","").replace('"',"").replace("<","").replace(">","").replace("|","")

    req.urlretrieve(x.get_attribute('src') , f'./GOOGLE/{safe_title}.jpg')
    num+=1

browser.close()