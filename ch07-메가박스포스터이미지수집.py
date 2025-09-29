import requests
import bs4 
import urllib.request as req
import os


code = requests.get('http://books.toscrape.com/')

soup = bs4.BeautifulSoup(code.text , 'html.parser')

result = soup.select('div.image_container img')
print(result)
result2 = soup.select('h3 > a')
result3 = soup.select('div.product_price > p.price_color')

if not os.path.exists('./CGV'):
        os.mkdir('./CGV')

num = 0
for x, y in zip(result, result2):
    print(f'제목:{y.text}')
    # print(x.attrs['src'])

    url = 'http://books.toscrape.com/'+x.attrs['src']

    req.urlretrieve(url, f"CGV/{y.text}.jpg")

    num +=1
    print('-'*100)
    

