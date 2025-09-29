import requests
import bs4

keyword = input('키워드 입력해 > ')
code = requests.get(f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}&ackey=h78xpm2r')

code2 = bs4.BeautifulSoup(code.text , 'html.parser')

result = code2.select('div.tit')

for i , x in enumerate(result):
    print(x )



