from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
import tqdm
from IPython.display import Image
import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium import webdriver
import time
import numpy as np
import pandas as pd

html = requests.get(f"https://www.op.gg/summoner/userName={quote_plus('내내내내박자')}")
soup = BeautifulSoup(html.text, 'html.parser')
containers = soup.findAll('div',{'class':'GameItemWrap'})

def clickbtn():
    driver = webdriver.Chrome('chromedriver')
    driver.get("https://www.op.gg")
    time.sleep(1)
    search = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/input')
    search.send_keys('내내내내박자')
    time.sleep(1)
    
    search.send_keys(Keys.ENTER)
    time.sleep(1.5)
    
    btnlist = []
    for i in range(4,30):
        btnlist.append(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[{i}]/a')
    
    a = soup.findAll('div', {'class':'GameItemWrap'})[-1].div['data-game-time']
    num = 0
    while True :
        driver.find_element_by_xpath(btnlist[num]).click()
        num +=1
        time.sleep(1.5)
        a = soup.findAll('div', {'class':'GameItemWrap'})[-1].div['data-game-time']
        
        if num == 16:
            break
    return

clickbtn()