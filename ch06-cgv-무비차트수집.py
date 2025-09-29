import requests
import bs4

code = requests.get('https://quotes.toscrape.com/')

#print(code.text)

soup = bs4.BeautifulSoup(code.text , 'html.parser')

#print(soup)
#print()
# title = soup.select_one('span.text')

# print(title.text)

title = soup.select('span.text')

for i , x in enumerate(title):
    print(f'{i+1} 번째 , {x.text}')