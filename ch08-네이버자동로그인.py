import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys , ActionChains
import platform
import pyperclip

def copy_and_paste(browser, css ,user_input):
    pyperclip.copy(user_input)
    browser.find_element(By.CSS_SELECTOR , css).click()
    os_type = platform.system()
    if os_type == 'Windows':
        paste_key = Keys.CONTROL
    else:
        paste_key = Keys.COMMAND

    ActionChains(browser).key_down(paste_key).key_down('V').perform()

opt = webdriver.ChromeOptions()

opt.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=opt)

browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')

time.sleep(1)

# id = browser.find_element(By.CSS_SELECTOR , 'input#id' )
# id.send_keys('kwonsunny')
copy_and_paste(browser , 'input#id' , 'kwonsunny')
time.sleep(1)
copy_and_paste(browser , 'input#pw' , 'kk011022kk')
time.sleep(1)
# pw = browser.find_element(By.CSS_SELECTOR , 'input#pw')
# pw.send_keys('kk011022kk')

browser.find_element(By.CSS_SELECTOR , 'button.btn_login').click()

time.sleep(2)