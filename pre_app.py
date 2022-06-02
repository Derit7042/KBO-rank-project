from flask import Flask, render_template, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

import schedule
import time

from pymongo import MongoClient
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/kbo', methods=['GET'])
def listing():
    kbo_rank = list(db.kbo.find({}, {'_id': False}))
    return jsonify({'kbo_ranks': kbo_rank})


## API 역할을 하는 부분
@app.route('/kbo', methods=['POST'])
def saving():



    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://sports.news.naver.com/kbaseball/record/index?category=kbo', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

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

            # db.kbo.delete_many({})




            doc = {
                'rank': rank,
                'name': name,
                'total': total,
                'win': win,
                'draw': draw,
                'lose': lose,
                'win_rate': win_rate,
                'gap': gap,
                'conti': gap
            }



            # db.kbo.delete_one({'name': 'SSG'})
            # db.kbo.delete_one({'name': '키움'})
            # db.kbo.delete_one({'name': 'KIA'})
            # db.kbo.delete_one({'name': 'LG'})
            # db.kbo.delete_one({'name': '삼성'})
            # db.kbo.delete_one({'name': '두산'})
            # db.kbo.delete_one({'name': '롯데'})
            # db.kbo.delete_one({'name': 'KT'})
            # db.kbo.delete_one({'name': '한화'})
            # db.kbo.delete_one({'name': 'NC'})


            # db.kbo.insert_one(doc)

            # db.kbo.update_one({'rank': '1'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '1'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '1'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '1'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '1'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '1'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '1'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '1'}, {'$set': {'conti': conti}})
            #
            # db.kbo.update_one({'rank': '2'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '2'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '2'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '2'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '2'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '2'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '2'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '2'}, {'$set': {'conti': conti}})
            #
            # db.kbo.update_one({'rank': '3'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '3'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '3'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '3'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '3'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '3'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '3'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '3'}, {'$set': {'conti': conti}})
            #
            # db.kbo.update_one({'rank': '4'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '4'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '4'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '4'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '4'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '4'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '4'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '4'}, {'$set': {'conti': conti}})
            #
            # db.kbo.update_one({'rank': '5'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '5'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '5'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '5'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '5'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '5'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '5'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '5'}, {'$set': {'conti': conti}})
            #
            # db.kbo.update_one({'rank': '6'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '6'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '6'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '6'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '6'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '6'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '6'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '6'}, {'$set': {'conti': conti}})
            #
            # db.kbo.update_one({'rank': '7'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '7'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '7'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '7'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '7'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '7'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '7'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '7'}, {'$set': {'conti': conti}})
            #
            # db.kbo.update_one({'rank': '8'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '8'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '8'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '8'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '8'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '8'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '8'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '8'}, {'$set': {'conti': conti}})
            #
            # db.kbo.update_one({'rank': '9'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '9'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '9'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '9'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '9'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '9'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '9'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '9'}, {'$set': {'conti': conti}})
            #
            # db.kbo.update_one({'rank': '10'}, {'$set': {'name': name}})
            # db.kbo.update_one({'rank': '10'}, {'$set': {'total': total}})
            # db.kbo.update_one({'rank': '10'}, {'$set': {'win': win}})
            # db.kbo.update_one({'rank': '10'}, {'$set': {'draw': draw}})
            # db.kbo.update_one({'rank': '10'}, {'$set': {'lose': lose}})
            # db.kbo.update_one({'rank': '10'}, {'$set': {'win_rate': win_rate}})
            # db.kbo.update_one({'rank': '10'}, {'$set': {'gap': gap}})
            # db.kbo.update_one({'rank': '10'}, {'$set': {'conti': conti}})





            # db.kbo.update_many({'rank': rank,
            #     'name': name,
            #     'total': total,
            #     'win': win,
            #     'draw': draw,
            #     'lose': lose,
            #     'win_rate': win_rate,
            #     'gap': gap,
            #     'conti': conti},{'$set':{'rank': rank,
            #     'name': name,
            #     'total': total,
            #     'win': win,
            #     'draw': draw,
            #     'lose': lose,
            #     'win_rate': win_rate,
            #     'gap': gap,
            #     'conti': conti}})



            db.kbo.update_many({'rank': rank}, {'$set':{'name': name, 'total': total, 'win': win, 'draw': draw, 'lose': lose, 'win_rate': win_rate, 'gap': gap, 'conti': conti}})



            # db.kbo.update_one({'rank': rank}, {'$set': {'rank': rank}})

            # kbo_rank = (rank, name, total, win, draw, lose, win_rate, gap, conti)
    return jsonify({'msg': ''})

# schedule.every(10).minutes.do(saving)
# schedule.every(10).minutes.do(listing)
# schedule.every(1).seconds.do(home)
# schedule.every(1).seconds.do(saving)
# schedule.every(1).seconds.do(listing)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)






#_tab_box_kbo > div > ul > li:nth-child(1) > div.vs_list.vs_list1 > div > div
#_tab_box_kbo > div > ul > li:nth-child(1) > div.vs_list.vs_list2 > div > div

#_tab_box_kbo > div > ul > li:nth-child(2) > div.vs_list.vs_list1 > div > div
#_tab_box_kbo > div > ul > li:nth-child(2) > div.vs_list.vs_list2 > div > div




#_tab_box_kbo > div > ul > li:nth-child(1) > div.vs_list.vs_list1 > div > div
#_tab_box_kbo > div > ul > li:nth-child(1) > div.vs_list.vs_list2 > div > div

#_tab_box_kbo > div > ul > li:nth-child(2) > div.vs_list.vs_list1 > div > div
#_tab_box_kbo > div > ul > li:nth-child(2) > div.vs_list.vs_list2 > div > div






#------------------------------------------------------
    # rank_list = tr.select('th > strong')

    # if rank_list is not None:
    #     print(rank_list)

        # rank = rank_list.text
        # print(rank)

        # rank_str = str(rank_list[0])
        # if '<' in str(rank_str)[8:10]:
        #     rank = rank_str[8:9]
        # else:
        #     rank = rank_str[8:10]
        # print(rank)
#------------------------------------------------------


# 각각의 줄
#regularTeamRecordList_table > tr:nth-child(1)
#regularTeamRecordList_table > tr:nth-child(2)

# 순위
#regularTeamRecordList_table > tr:nth-child(1) > th > strong
#regularTeamRecordList_table > tr:nth-child(2) > th > strong

# 팀명
#regularTeamRecordList_table > tr:nth-child(1) > td.tm
#regularTeamRecordList_table > tr:nth-child(2) > td.tm


# 경기수
#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(3) > span

# 승
#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(4) > span

# 무
#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(6) > span

# 패
#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(5) > span

# 승률
#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(7) > strong

# 게임차
#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(8) > span