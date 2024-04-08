'''
    Парсинг сайта startupstash.com
    Собираем информацию о стартапах
'''

import re
from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp
import json
import time


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'
}

dict_all_startups = {}


def time_tracker(foo):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = foo(*args, **kwargs)
        end = time.time() - start
        print(f'{foo.__name__} выполнялась {end:.2f} сек.')
        return result
    return wrapper


def get_html(url):
    get_request = requests.get(url, headers=headers)
    return get_request.text


async def async_get_startup_info(index, startup, session: aiohttp.ClientSession):
    async with session.get(startup.find('h2').find('a').get('href')) as response:
        if response.status != 200:
            print(response.status)
        startup_soup = BeautifulSoup(await response.text(encoding='UTF-8'), 'lxml')
        if startup_soup.find(class_='dec'):
            startup_description = '\n'.join([el.text for el in startup_soup.find(class_='dec').find_all('p')])
        else:
            startup_description = ''
            print(startup.find('h2').find('a').text)
        dict_all_startups[index] = {
            'Name': startup.find('h2').find('a').text,
            'Description': startup_description.lstrip(),
            'Link': startup.find('h2').find('a').get('href'),
            'Logo': startup.find(class_='tool-img v-yes').find('img').get('src') if startup.find(
                class_='tool-img v-yes') else '',
            'Category': startup.find(class_='cate').find('a').text
        }
        # print(f'{index}) ' + dict_all_startups[index]['Name'] + ' - сохранен')


async def async_main():
    '''
        Разбор страницы и сохранение даных по всем стартапам в json
    '''

    with open('startupstash.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')

    # print(len(soup.find_all('div', class_=re.compile(r'trello-box main-t-s'))))
    all_startups = soup.find_all(class_=re.compile(r'trello-box main-t-s'))

    tasks = []
    async with aiohttp.ClientSession() as session:
        for index, startup in enumerate(all_startups):
            tasks.append(async_get_startup_info(index=index, startup=startup, session=session))
            if index == 100:
                break
        await asyncio.gather(*tasks)

    with open('startupstash.json', 'w', encoding='utf-8') as f:
        json.dump(dict_all_startups, f, ensure_ascii=False, indent=4)


@time_tracker
def main():
    asyncio.run(async_main())


def save_page():
    '''
        Скачиваем необходимую страницу
    '''

    url = 'https://startupstash.com/explore/'
    # get_html(url)
    with open('startupstash.html', 'w', encoding='utf-8') as outfile:
        outfile.write(get_html(url))


if __name__ == '__main__':
    # save_page()
    main()
