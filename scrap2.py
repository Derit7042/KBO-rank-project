import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/news/index?isphoto=N', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#_newsList > ul > li:nth-child(1) > div > a > span
#_newsList > ul > li:nth-child(2) > div > a > span
#_newsList > ul > li:nth-child(3) > div > a > span
#_newsList > ul > li:nth-child(1) > div > a > span


print(soup)

# trs = soup.select('#_newsList > ul > li:nth-child(1)')
# print(trs)
# for tr in trs:
#     tr_articles = tr.select('div > a > span')
#     print(tr_articles)

#웹사이트의 구조를 알아야한다. 사이트에 들어갈 때 모든 정보를 요청을 하는 거면 무거워질 수 밖에 없다.
#무거우면 속도가 느려지는데, CSR이라고 하는데, 완전히 맞는건 아니고, bs4랑 requests로 가능했던 것은
#SSI 같이 전부 만들어서 오는 것이다. 지금 이런 사이트는 CSR 이라고 해서 그래서 크롤링이 안 된다.
#그래서 셀레니움이라는게 있는데, 저 사이트를 열어서, 추가적인 데이터를 가져오는 구조? CSR
#그 사이트를 들어가는 작업을 해줘야한다.
#