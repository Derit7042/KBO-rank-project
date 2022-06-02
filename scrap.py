import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index?category=kbo', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#regularTeamRecordList_table > tr:nth-child(1) > th > strong
#regularTeamRecordList_table > tr:nth-child(1) > td.tm

trs = soup.select('#regularTeamRecordList_table > tr')
for tr in trs:
    th_rank = tr.select('th')
    rank = th_rank[0].text
    if rank is not None:
        td_name = tr.select('td.tm')
        name = td_name[0].text.strip()

        td_total = tr.select('td:nth-child(3) > span')
        total = td_total[0].text

        td_win = tr.select('td:nth-child(4) > span')
        win = td_win[0].text

        td_draw = tr.select('td:nth-child(6) > span')
        draw = td_draw[0].text

        td_lose = tr.select('td:nth-child(5) > span')
        lose = td_lose[0].text

        td_win_rate = tr.select('td:nth-child(7) > strong')
        win_rate = td_win_rate[0].text

        td_gap = tr.select('td:nth-child(8) > span')
        gap = td_gap[0].text

        td_conti = tr.select('td:nth-child(9) > span')
        conti = td_conti[0].text

        print(rank, name, total, win, draw, lose, win_rate, gap, conti)