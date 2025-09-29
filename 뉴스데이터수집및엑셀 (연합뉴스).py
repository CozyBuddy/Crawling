import selenium
from selenium import webdriver
import time
from selenium.webdriver import ActionChains ,Keys
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import bs4
import re
from datetime import datetime
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import tempfile
opt = webdriver.ChromeOptions()
temp_profile_dir = tempfile.mkdtemp() # <- solution
opt.add_argument(f"--user-data-dir={temp_profile_dir}")
opt.add_argument('--headless')
opt.add_experimental_option("prefs", {
    "profile.managed_default_content_settings.images": 2,
    "profile.managed_default_content_settings.plugins": 2
})

# opt.add_argument(f"--user-data-dir=/tmp/chrome_data_{debug_port}") 
# opt.add_argument(f"--remote-debugging-port={debug_port}")


opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/140.0.7339.208 Safari/537.36")
opt.add_argument("--disable-blink-features=AutomationControlled"); 
browser = webdriver.Chrome(options=opt)
browser.set_page_load_timeout(300)
browser.implicitly_wait(10)


## 연합뉴스
wb2 = Workbook()
ws2 = wb2.active
excelnum2 = 1


browser.get(f'https://www.yna.co.kr/sitemap/')


results = browser.find_elements(By.CSS_SELECTOR , 'div.link-field01 ul.link-zone01 a' )
#results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

href_list = [el.get_attribute('href') for el in results]
# href_list2 = [el.get_attribute('href') for el in results2]
for a in href_list:
    
    browser.get(a)
    result3 = browser.find_elements( By.CSS_SELECTOR  , 'div.link-zone02 a')
    #print(result3.text)

    href_list = [el.get_attribute('href') for el in result3]
    for i in href_list:

        browser.get(i)
        result3 = browser.find_elements(By.CSS_SELECTOR , 'div.link-zone03 a')

        href_list2 = [el.get_attribute('href') for el in result3]
        for i in href_list2:
            browser.get(i)
            time.sleep(5)
            result3 = browser.find_element(By.CSS_SELECTOR , 'div.story-news.article')
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws2[f"A{excelnum2+1}"] = i 
                    excelnum2+=1

wb2.save(f'뉴스기사수집(연합뉴스){datetime.now().date()}.xlsx')     

