import requests
import bs4



code = requests.get('https://underkg.co.kr/index.php?mid=news&page=1')

soup = bs4.BeautifulSoup(code.text , 'html.parser')

result = soup.select('div.content h1.title a')

for x , y in enumerate(result):
    print(x, y.text)
    print(y.attrs['href'])

    code_news = requests.get(y.attrs['href'])
    soup_news = bs4.BeautifulSoup(code_news.text , 'html.parser')

    result = soup_news.select_one('div.read_body')

    print(result.text)