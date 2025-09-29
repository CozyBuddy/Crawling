import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

keyword = input('키워드 입력 >')
opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=opt)

blog_url_list = []

for page_num in range(1,6):
    browser.get(f'https://section.blog.naver.com/Search/Post.naver?pageNo={page_num}&rangeType=ALL&orderBy=sim&keyword={keyword}')
    time.sleep(2)
    items = browser.find_elements(By.CSS_SELECTOR,  'a.desc_inner')
    for i in items:
        blog_url_list.append(i.get_attribute('href'))

# print(blog_url_list)

for i in blog_url_list:
    rei = i.replace('https://blog.naver' , 'https://m.blog.naver')

    browser.get(rei)
    time.sleep(2)

    title =browser.find_element( By.CSS_SELECTOR ,'div.se-title-text.se-module-text span')
    content = browser.find_element(By.CSS_SELECTOR ,'div.se-main-container')

    print(title.text)
    print(content.text)

    print('-'*100)
