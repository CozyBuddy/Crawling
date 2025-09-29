import requests
import bs4

code = requests.get('https://finance.naver.com/marketindex')

soup = bs4.BeautifulSoup(code.text , 'html.parser')

price = soup.select('ul#exchangeList span.value')

for i ,x in enumerate(price):
    print(x.text)