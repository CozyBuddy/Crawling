from selenium import webdriver
import time
from selenium.webdriver import ActionChains , Keys
from openpyxl import Workbook
from selenium.webdriver.common.by import By
opt = webdriver.ChromeOptions()
opt.add_argument("--disable-gpu")   # GPU 가속 끄기
opt.add_argument("--disable-software-rasterizer")  # 소프트웨어 렌더링도 끄기
opt.add_experimental_option('detach',True) #자동으로 안 닫히게 하는역할
opt.add_experimental_option("prefs", {
    "profile.managed_default_content_settings.images": 2,
    "profile.managed_default_content_settings.plugins": 2
})
opt.add_argument('--headless')

browser = webdriver.Chrome(options=opt)
browser.get('https://www.youtube.com/watch?v=NMjhjrBIrG8&list=RDNMjhjrBIrG8&start_radio=1')
browser.implicitly_wait(10)

prev_height = 0
same_num_cnt = 0
while True:
    ActionChains(browser).key_down(Keys.PAGE_DOWN).perform()
    
    time.sleep(4)
    cur_height = browser.execute_script('return document.documentElement.scrollHeight')
    print(cur_height)
    if prev_height >= cur_height :
        same_num_cnt+=1
    else:
        same_num_cnt=0

    if same_num_cnt > 20 :
        break
    prev_height = cur_height

comments = browser.find_elements(By.CSS_SELECTOR , '#content-text')
wb = Workbook()
ws = wb.active
for x,i in enumerate(comments):
    print(i.text.replace('\n','').strip())
    ws[f'A{x+1}'] =  i.text.replace('\n','').strip()

wb.save('유튜브댓글수집.xlsx')
browser.close()







