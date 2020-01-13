from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
import tqdm
from IPython.display import Image
import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
import numpy as np
import pandas as pd

# 게임 한칸의 모음들을 가져옴(containers)
html = requests.get(f"https://www.op.gg/summoner/userName={quote_plus('내내내내박자')}")
soup = BeautifulSoup(html.text, 'html.parser')
containers = soup.findAll('div',{'class':'GameItemWrap'})


filename = 'Poppy.csv'
f = open(filename, 'w')

headers = 'Summoner_id,Game_id,Game_type,Game_start_time,Game_length,Win_lose,Champion,Rune,Kill,Death,Assist,KDA,Level,CS,CS_per_M,KP,Tier_average,My_TOP,My_JG,My_MID,My_AD,My_SUP,Enemy_TOP,Enemy_JG,Enemy_MID,Enemy_AD,Enemy_SUP\n' 

f.write(headers)
for container in containers:
    Summoner_id = container.div['data-summoner-id']
    Game_id = container.div['data-game-id']     
    url = f"https://www.op.gg/summoner/matches/ajax/detail/gameId={Game_id}&summonerId={Summoner_id}"
    html2 = requests.get(url)
    soup2 = BeautifulSoup(html2.text, 'html.parser')

    Game_type = container.div('div', {'class':'GameType'})[0].text.strip()
    Game_start_time = container.div('div', {'class':'TimeStamp'})[0].text.strip()
    Game_length = container.div('div', {'class':'GameLength'})[0].text.strip()
    Win_lose = container.div['class'][-1]
    Champion = container.div.a.img['alt']
    Rune = container.div('div', {'class':'Rune'})[0].img['alt']
    Kill = container.div('div', {'class':'KDA'})[0].div.select('span')[0].text
    Death = container.div('div', {'class':'KDA'})[0].div.select('span')[1].text
    Assist = container.div('div', {'class':'KDA'})[0].div.select('span')[2].text
    KDA = container.div('div', {'class':'KDARatio'})[0].text.strip().split()[0]
    Level = container.div('div', {'class':'Level'})[0].text.strip().replace('Level','')
    CS = container.div('span', {'class':'CS tip'})[0].text.split()[0]
    CS_per_M = container.div('span', {'class':'CS tip'})[0].text.split()[1].strip('()')
    KP = container.div('div', {'class':'CKRate tip'})[0].text.strip().split()[-1].replace('%','')
    Tier_average = container.div('b')[0].text

    contents = soup2.findAll('a')[4:]
    content = contents[::2]

    ATeam = []
    for i in content:
        ATeam.append(i.div.text)

    My_TOP = ATeam[0]
    My_JG = ATeam[1]
    My_MID = ATeam[2]
    My_AD = ATeam[3]
    My_SUP = ATeam[4]
    Enemy_TOP = ATeam[5]
    Enemy_JG = ATeam[6]
    Enemy_MID = ATeam[7]
    Enemy_AD = ATeam[8]
    Enemy_SUP = ATeam[9]

    My_item = soup2.findAll('tr', {'class':'Row'})[1:5]

#     itemlist = []

#     for i in My_item[0].findAll('div', {'class':'Item'}):
#         itemlist.append(i.img['alt'])

#     for i in range(len(itemlist)):
#         if len(itemlist) == 7:
#             Item_0 = itemlist[0]
#             Item_1 = itemlist[1]
#             Item_2 = itemlist[2]
#             Item_3 = itemlist[3]
#             Item_4 = itemlist[4]
#             Item_5 = itemlist[5]
#             Item_6 = itemlist[6]
#         else:
#             Item_0 = itemlist[0]
#             Item_1 = itemlist[1]
#             Item_2 = itemlist[2]
#             Item_3 = itemlist[3]
#             Item_4 = itemlist[4]
#             Item_5 = itemlist[5]
        

    f.write(Summoner_id + "," + Game_id + "," + Game_type + "," + Game_start_time + "," + Game_length + "," + Win_lose + "," + Champion + "," + Rune + "," + Kill + "," + Death + "," + Assist + "," + KDA + "," + Level + "," + CS + "," + CS_per_M + "," + KP + "," + Tier_average + "," + My_TOP + "," + My_JG + "," + My_MID + "," + My_AD + "," + My_SUP + "," + Enemy_TOP + "," + Enemy_JG + "," + Enemy_MID + "," + Enemy_AD + "," + Enemy_SUP +'\n')
    
f.close()