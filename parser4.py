import json
import re
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import time
from googletrans import Translator
from translit import *

auto_catalog = {}
auto_logos = {}
headers = {
    'Accept': '*/*',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'
}
page_counter = 0
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def counter(foo):
    async def wrapper(*args, **kwargs):
        global page_counter
        await foo(*args, **kwargs)
        page_counter -= 1
        print(f'Осталось:{page_counter}')
        return foo
    return wrapper


def get_response(url):
    response = requests.get(url, headers=headers)
    return response


def save_page(url, file_path):
    source = get_response(url)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(source.text)


def find_mark_in_logo_dict(mark):
    for logo in auto_logos.items():
        if re.search(r'\b' + mark.lower() + r'\b', logo[1]['info'].lower()):
            return logo[0]


async def async_save_page(url, file_path, session):
    async with session.get(url) as response:
        if response.status != 200:
            print(response.status)
        else:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(await response.text(encoding='UTF-8'))


async def async_save_img(url, file_path, session):
    async with session.get(url) as response:
        with open(file_path, 'wb') as img_file:
            img_file.write(await response.content.read())


async def async_save_logos(url):
    await asyncio.sleep(1)
    source = get_response(url)
    with open(f'AutoCatalog/', 'w', encoding='utf-8') as file:
        file.write(source.text)
    Path(f'AutoCatalog/{url.text}').mkdir(parents=True, exist_ok=True)
    # auto_logos[name] = {
    #                 'Link': link
    #             }


async def translit(input_string, session):
    '''
        Функция для транслита текста
    '''
    params = {
        'ui': 'ru',
        'text': input_string,
        'lang': 'en-ru'
    }
    url = "https://dictionary.yandex.net/dicservice.json/lookup"
    async with session.get(url, headers=headers, params=params) as response:
        if response.status != 200:
            print(response.status)
        else:
            return await response.json()['def'][0]['tr'][0]['text']


async def async_trasliterate():
    tasks = []
    global auto_logos
    with open('AutoCatalog/_AutoLogos_/auto_logos.json', 'r', encoding='utf-8') as json_file:
        auto_logos = json.load(json_file)
    async with aiohttp.ClientSession() as session:
        for logo in auto_logos.items():
            ...


async def async_parsing():
    tasks = []
    global page_counter
    global auto_catalog
    global auto_logos


    '''
        Блок скачивания html страниц с подробной информацией о логотипах разных марок 
    '''
    # async with aiohttp.ClientSession() as session:
    #     for i in range(4):
    #         with open(f'car_logos_page{i+1}.html', 'r', encoding='utf-8') as file:
    #             source = file.read()
    #         soup = BeautifulSoup(source, 'lxml')
    #         for el in soup.find_all(class_='meta-image'):
    #             name = el.find('a').get('title')
    #             tasks.append(async_save_page(el.find('a').get('href'),
    #                                          f'AutoCatalog/_AutoLogos_/{name}.html',
    #                                          session))
    #             auto_logos[name] = {
    #                 'html_file': name + '.html'
    #             }
    #     with open('AutoCatalog/_AutoLogos_/auto_logos.json', 'w', encoding='utf-8') as json_file:
    #         json.dump(auto_logos, json_file, indent=4, ensure_ascii=False)
    #     page_counter = len(tasks)
    #     start = time.time()
    #     print(f'Старт сохранения страниц...')
    #     await asyncio.gather(*tasks)
    #     print(f'Сохранено за {time.time() - start:.2f}с')

    '''
        Блок парсинга инфомации о логотипах и скачивания img файлов логотипов 
    '''
    # with open('AutoCatalog/_AutoLogos_/auto_logos.json', 'r', encoding='utf-8') as json_file:
    #     auto_logos = json.load(json_file)
    # async with aiohttp.ClientSession() as session:
    #     print(f'Парсинг html файлов...')
    #     for logo in auto_logos.items():
    #         with open('AutoCatalog/_AutoLogos_/' + logo[1]['html_file'], 'r', encoding='utf-8') as f:
    #             soup = BeautifulSoup(f.read(), 'lxml')
    #             try:
    #                 if soup.find(class_=re.compile(r'wp-block-image')).find('a'):
    #                     tasks.append(async_save_img(soup.find(class_=re.compile(r'wp-block-image')).find('a').attrs['href'],
    #                             f'AutoCatalog/_AutoLogos_/{logo[0]}.png',
    #                              session))
    #                     auto_logos[logo[0]]['img_file'] = f'{logo[0]}.png'
    #                 else:
    #                     tasks.append(
    #                         async_save_img(soup.find(class_=re.compile(r'wp-block-image')).find('img').get('data-src'),
    #                                        f'AutoCatalog/_AutoLogos_/{logo[0]}.png',
    #                                        session))
    #                     auto_logos[logo[0]]['img_file'] = f'{logo[0]}.png'
    #             except Exception as e:
    #                 print(f'Ошибка при сохранении лого марки \'{logo[0]}\'')
    #     start = time.time()
    #     print(f'Сохранения логотипов...')
    #     await asyncio.gather(*tasks)
    #     print(f'Сохранения логотипов завершено (время выполнения задачи - {time.time() - start:.2f}с)')
    # with open('AutoCatalog/_AutoLogos_/auto_logos.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(auto_logos, json_file, indent=4, ensure_ascii=False)


def sync_parsing():
    global auto_logos
    global auto_catalog
    '''
        Блок парсинга инфомации о логотипах 
    '''
    # with open('AutoCatalog/_AutoLogos_/auto_logos.json', 'r', encoding='utf-8') as json_file:
    #     auto_logos = json.load(json_file)
    # print(f'Парсинг html файлов...')
    # start = time.time()
    # for logo in auto_logos.items():
    #     with (open('AutoCatalog/_AutoLogos_/' + logo[1]['html_file'], 'r', encoding='utf-8') as f):
    #         soup = BeautifulSoup(f.read(), 'lxml')
    #         try:
    #             soup_dict = {
    #                 'review': soup.find(class_=re.compile(r'wp-block-table')).find(
    #                     lambda tag: tag.text == 'Обзор') if soup.find(class_=re.compile(r'wp-block-table')) else None,
    #                 'info': soup.find(class_='entry-content').find_all('p')
    #             }
    #             if soup_dict['review']:
    #                 auto_logos[logo[0]]['info'] = re.sub(r'<.*?>', '',
    #                                                      str(soup_dict['review'].find_next_siblings('td'))[1:-1])
    #             elif soup_dict['info']:
    #                 auto_logos[logo[0]]['info'] = re.sub(r'<.*?>', '', str(soup_dict['info'][1:])[1:-1])
    #             else:
    #                 auto_logos[logo[0]]['info'] = ''
    #         except Exception as e:
    #             print(f'Ошибка при парсинге \'{logo[0]}\'')
    # print(f'Парсинг html файлов завершен (время выполнения задачи - {time.time() - start:.2f}с)')
    # with open('AutoCatalog/_AutoLogos_/auto_logos.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(auto_logos, json_file, indent=4, ensure_ascii=False)

    '''
        Консолидация информации из файлов auto_catalog.json и auto_logos.json
    '''
    #
    # with open('AutoCatalog/_AutoLogos_/auto_logos.json', 'r', encoding='utf-8') as json_file:
    #     auto_logos = json.load(json_file)
    # with open('AutoCatalog/auto_catalog.json', 'r', encoding='utf-8') as json_file:
    #     auto_catalog = json.load(json_file)
    #
    # for mark in auto_catalog:
    #     auto_catalog[mark]['link'] = [auto_catalog[mark]['link'],
    #                                   'https://' + re.findall(r'(\w+)/$', auto_catalog[mark]['link'])[0] + '.drom.ru']
    #     if mark in auto_logos:
    #         auto_catalog[mark]['logo'] = 'AutoCatalog/_AutoLogos_/' + auto_logos[mark]['img_file']
    #         auto_catalog[mark]['info'] = auto_logos[mark]['info']
    #     else:
    #         finder = find_mark_in_logo_dict(mark)
    #         if finder:
    #             auto_catalog[mark]['logo'] = 'AutoCatalog/_AutoLogos_/' + auto_logos[finder]['img_file']
    #             auto_catalog[mark]['info'] = auto_logos[finder]['info']
    #         else:
    #             auto_catalog[mark]['logo'] = ''
    #             auto_catalog[mark]['info'] = ''
    #
    # with open('AutoCatalog/auto_catalog.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(auto_catalog, json_file, indent=4, ensure_ascii=False)

    with open('AutoCatalog/auto_catalog.json', 'r', encoding='utf-8') as json_file:
        auto_catalog = json.load(json_file)
    session = requests.Session()
    # for mark in auto_catalog:
    mark = 'DW Hower'
    if not auto_catalog[mark]['logo']:
        try:
            response = session.get(auto_catalog[mark]['link'][1])
            soup = BeautifulSoup(response.text, 'lxml')
            img_link = 'https:' + soup.find(class_='b-flex b-flex_align_left').find('img').get('src')

            if img_link:
                with open('AutoCatalog/_AutoLogos_/' + mark + '.png', 'wb') as img_file:
                    img_file.write(get_response(img_link).content)
                auto_catalog[mark]['logo'] = 'AutoCatalog/_AutoLogos_/' + mark + '.png'
                print(auto_catalog[mark])
        except Exception as e:
            print('Error - ' + auto_catalog[mark])

    if not auto_catalog[mark]['info']:
        try:
            response = session.get('https://1000logos.net/' + mark.lower() + '-logo/')
            soup = BeautifulSoup(response.text, 'lxml')
            img_link = 'https:' + soup.find(class_='b-flex b-flex_align_left').find('img').get('src')

            if img_link:
                with open('AutoCatalog/_AutoLogos_/' + mark + '.png', 'wb') as img_file:
                    img_file.write(get_response(img_link).content)
                auto_catalog[mark]['info'] = 'AutoCatalog/_AutoLogos_/' + mark + '.png'
                print(auto_catalog[mark])
        except Exception as e:
            print('Error - ' + auto_catalog[mark])


def main():
    # url = 'https://www.drom.ru/catalog/'
    # save_page(url, 'auto_catalog.html')

    # sync_parsing()

    # asyncio.run(async_parsing())

    translator = Translator()
    # print(translator.translate('lander', src='en', dest='ru'))

    # print(re.findall(r'(\w+)/$', 'https://www.drom.ru/catalog/audi/')[0])


    '''
        Правка данных в файле auto_catalog.json
    '''
    session = requests.Session()
    with open('AutoCatalog/auto_catalog.json', 'r', encoding='utf-8') as json_file:
        auto_catalog = json.load(json_file)
    for key, value in auto_catalog.items():
        alt_name = re.findall(r'(\w+)/$', value['link'][0])[0]
        value['alt_name'] = alt_name
        if alt_name.count('_'):
            value['alt_name'] = alt_name.replace('_', '-')

        if key == 'Audi':
            try:
                response = session.get(value['link'][0])
                soup = BeautifulSoup(response.text, 'lxml')
                rus_name = 'https:' + soup.find(class_='b-flex b-flex_align_left').find('img').get('src')

                value['rus_name']
                print(translit_eng_to_ru(key))
                print(alt_name + '\n')
            except:
                print('Error - ' + alt_name)

    # with open('AutoCatalog/auto_catalog.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(auto_catalog, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
