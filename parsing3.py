'''
    Парсинг сайта startupstash.com
    Собираем информацию о стартапах
'''
import re

from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time


def get_html(url):
    # session = requests.Session()
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'
    }
    get_request = requests.get(url, headers=headers)
    print(get_request.status_code)
    return get_request.text


'''
    Скачиваем страницу
'''

# url = 'https://startupstash.com/explore/'
# # get_html(url)
# with open('startupstash.html', 'w', encoding='utf-8') as outfile:
#     outfile.write(get_html(url))


'''
    Разбор страницы
'''
#
with open('startupstash.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'lxml')

dict_all_startups = {}
print(len(soup.find_all('div', class_=re.compile(r'trello-box main-t-s'))))

# all_startups = soup.find_all(class_='trello-box main-t-s')
# for index, startup in enumerate(all_startups):
#     dict_all_startups[startup.find('h2').find('a').text] = startup.find('h2').find('a').get('href')
#
# print(dict_all_startups)
