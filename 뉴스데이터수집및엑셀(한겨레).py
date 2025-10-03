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
temp_profile_dir = tempfile.mkdtemp() # <- solution

opt = webdriver.ChromeOptions()
opt.add_argument(f"--user-data-dir={temp_profile_dir}")
#opt.add_argument('--headless')
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
wait = WebDriverWait(browser, 10)

num = 1
wb = Workbook()
ws = wb.active
excelnum = 1
while True :
    if num >= 335 :
        break
    try:

        browser.get(f'https://www.hani.co.kr/arti/politics?page={num}')
        
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.BaseArticleCard_content__tYkEA >a')))

        #results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

        href_list = [el.get_attribute('href') for el in results]
    except Exception as e :
        num+=1
        print('에러' ,e)
        continue
   # href_list2 = [el.get_attribute('href') for el in results2]
    for a in href_list:
        try:
            browser.get(a)
            
            result3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-text')))
        
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws[f"A{excelnum+1}"] = i 
                    excelnum+=1

        except Exception as e:
            print(f"Error at {e}")
            continue
    if num >= 334 :
        break
    num+=1


num=1
while True :
    if num >= 335 :
        break
    try:

        browser.get(f'https://www.hani.co.kr/arti/society?page={num}')
        
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.BaseArticleCard_content__tYkEA >a')))

        #results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

        href_list = [el.get_attribute('href') for el in results]
    except Exception as e :
        num+=1
        print('에러' ,e)
        continue
   # href_list2 = [el.get_attribute('href') for el in results2]
    for a in href_list:
        try:
            browser.get(a)
            
            result3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-text')))
        
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws[f"A{excelnum+1}"] = i 
                    excelnum+=1

        except Exception as e:
            print(f"Error at {e}")
            continue
    if num >= 334 :
        break
    num+=1

num=1
while True :
    if num >= 335 :
        break
    try:

        browser.get(f'https://www.hani.co.kr/arti/area?page={num}')
        
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.BaseArticleCard_content__tYkEA >a')))

        #results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

        href_list = [el.get_attribute('href') for el in results]
    except Exception as e :
        num+=1
        print('에러' ,e)
        continue
   # href_list2 = [el.get_attribute('href') for el in results2]
    for a in href_list:
        try:
            browser.get(a)
            
            result3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-text')))
        
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws[f"A{excelnum+1}"] = i 
                    excelnum+=1

        except Exception as e:
            print(f"Error at {e}")
            continue
    if num >= 334 :
        break
    num+=1
    
num=1
while True :
    if num >= 335 :
        break
    try:

        browser.get(f'https://www.hani.co.kr/arti/economy?page={num}')
        
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.BaseArticleCard_content__tYkEA >a')))

        #results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

        href_list = [el.get_attribute('href') for el in results]
    except Exception as e :
        num+=1
        print('에러' ,e)
        continue
   # href_list2 = [el.get_attribute('href') for el in results2]
    for a in href_list:
        try:
            browser.get(a)
            
            result3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-text')))
        
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws[f"A{excelnum+1}"] = i 
                    excelnum+=1

        except Exception as e:
            print(f"Error at {e}")
            continue
    if num >= 334 :
        break
    num+=1

num=1
while True :
    if num >= 335 :
        break
    try:

        browser.get(f'https://www.hani.co.kr/arti/international?page={num}')
        
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.BaseArticleCard_content__tYkEA >a')))

        #results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

        href_list = [el.get_attribute('href') for el in results]
    except Exception as e :
        num+=1
        print('에러' ,e)
        continue
   # href_list2 = [el.get_attribute('href') for el in results2]
    for a in href_list:
        try:
            browser.get(a)
            
            result3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-text')))
        
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws[f"A{excelnum+1}"] = i 
                    excelnum+=1

        except Exception as e:
            print(f"Error at {e}")
            continue
    if num >= 334 :
        break
    num+=1

num=1
while True :
    if num >= 335 :
        break
    try:

        browser.get(f'https://www.hani.co.kr/arti/culture?page={num}')
        
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.BaseArticleCardVertical_card__LLa8l >a')))

        #results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

        href_list = [el.get_attribute('href') for el in results]
    except Exception as e :
        num+=1
        print('에러' ,e)
        continue
   # href_list2 = [el.get_attribute('href') for el in results2]
    for a in href_list:
        try:
            browser.get(a)
            
            result3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-text')))
        
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws[f"A{excelnum+1}"] = i 
                    excelnum+=1

        except Exception as e:
            print(f"Error at {e}")
            continue
    if num >= 334 :
        break
    num+=1
num=1

while True :
    if num >= 335 :
        break
    try:

        browser.get(f'https://www.hani.co.kr/arti/science?page={num}')
        
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.BaseArticleCard_content__tYkEA >a')))

        #results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

        href_list = [el.get_attribute('href') for el in results]
    except Exception as e :
        num+=1
        print('에러' ,e)
        continue
   # href_list2 = [el.get_attribute('href') for el in results2]
    for a in href_list:
        try:
            browser.get(a)
            
            result3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-text')))
        
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws[f"A{excelnum+1}"] = i 
                    excelnum+=1

        except Exception as e:
            print(f"Error at {e}")
            continue
    if num >= 334 :
        break
    num+=1

num=1
while True :
    if num >= 335 :
        break
    try:

        browser.get(f'https://www.hani.co.kr/arti/animalpeople?page={num}')
        
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.ArticleListTitle_link__U_6Bo')))

        #results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

        href_list = [el.get_attribute('href') for el in results]
    except Exception as e :
        num+=1
        print('에러' ,e)
        continue
   # href_list2 = [el.get_attribute('href') for el in results2]
    for a in href_list:
        try:
            browser.get(a)
            
            result3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-text')))
        
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws[f"A{excelnum+1}"] = i 
                    excelnum+=1

        except Exception as e:
            print(f"Error at {e}")
            continue
    if num >= 334 :
        break
    num+=1

num=1
while True :
    if num >= 335 :
        break
    try:

        browser.get(f'https://www.hani.co.kr/arti/opinion?page={num}')
        
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.BaseArticleCard_content__tYkEA >a')))

        #results2 = browser.find_elements(By.CSS_SELECTOR , 'div.section_article._TEMPLATE div.sa_text > a' )

        href_list = [el.get_attribute('href') for el in results]
    except Exception as e :
        num+=1
        print('에러' ,e)
        continue
   # href_list2 = [el.get_attribute('href') for el in results2]
    for a in href_list:
        try:
            browser.get(a)
            
            result3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-text')))
        
            splitresult = [s.strip().replace('=','').replace('@','') for s in result3.text.split('\n') if s.strip() ]

            for i in splitresult:
                if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", i) :
                    ws[f"A{excelnum+1}"] = i 
                    excelnum+=1

        except Exception as e:
            print(f"Error at {e}")
            continue
    if num >= 334 :
        break
    num+=1

wb.save(f'뉴스기사수집(한겨레){datetime.now().date()}.xlsx')


