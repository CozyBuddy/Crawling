from selenium import webdriver
from selenium.webdriver.common.by import By
import time
opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach' , True)

opt.add_argument(r"--user-data-dir=C:\selenium\ChromeProfile")  # 원하는 경로
opt.add_argument(r'--profile-directory=Default')  # 기본 프로필

browser = webdriver.Chrome(options=opt)
browser.get('https://accounts.kakao.com/login/?continue=https%3A%2F%2Fmail.daum.net#login')

id = browser.find_element(By.CSS_SELECTOR , 'input#loginId--1')
id.send_keys('kwonsunny@naver.com')

pw = browser.find_element(By.CSS_SELECTOR , 'input#password--2')
pw.send_keys('k011022k')
button = browser.find_element(By.CSS_SELECTOR ,'button.btn_g.highlight.submit')

button.click()
time.sleep(2)

title = browser.find_elements(By.CSS_SELECTOR , 'strong.tit_subject')

for i in title:
    print(i.text)

browser.close()