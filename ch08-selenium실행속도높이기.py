import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

keyword = input('키워드 입력 >')
opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)
opt.add_argument('--blink-settings=imagesEnabled=false')
opt.add_experimental_option(
    'prefs' , {'profile.managed_default_content_settings.images' : 2}
)
opt.add_argument('headless')
browser = webdriver.Chrome(options=opt)
browser.implicitly_wait(10)
blog_url_list = []

for page_num in range(1,10):
    browser.get(f'https://section.blog.naver.com/Search/Post.naver?pageNo={page_num}&rangeType=ALL&orderBy=sim&keyword={keyword}')
   
    items = browser.find_elements(By.CSS_SELECTOR,  'a.desc_inner')
    for i in items:
        blog_url_list.append(i.get_attribute('href'))

# print(blog_url_list)

for i in blog_url_list:
    rei = i.replace('https://blog.naver' , 'https://m.blog.naver')

    browser.get(rei)
   

    title =browser.find_element( By.CSS_SELECTOR ,'div.se-title-text.se-module-text span')
    content = browser.find_element(By.CSS_SELECTOR ,'div.se-main-container')

    print(title.text)
    print(content.text)

    print('-'*100)
