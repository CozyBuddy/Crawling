import requests
import bs4

searchword = input('입력 >')
for i in range(10):
    print(i)
    code = requests.get(f'https://kin.naver.com/search/list.naver?query={searchword}&page={i+1}')

    result = bs4.BeautifulSoup(code.text , 'html.parser')

    result2 =  result.select('a._nclicks\:kin\.txt._searchListTitleAnchor')
    result3 =  result.select('dd.txt_inline')

    for x , y in zip(result2 , result3):
        print(x.text , y.text)