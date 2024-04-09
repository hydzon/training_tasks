import re
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from pathlib import Path
import requests


auto_catalog = {}
auto_logos = {}

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'
}


def get_response(url):
    response = requests.get(url, headers=headers)
    return response


def save_page(url, file_path):
    source = get_response(url)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(source.text)


async def async_save_page(url, file_path):
    ...


async def async_parsing():
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(4):
            with open(f'car_logos_page{i+1}.html', 'r', encoding='utf-8') as file:
                source = file.read()
            soup = BeautifulSoup(source, 'lxml')
            for el in soup.find_all(class_='meta-image'):
                auto_logos[el.find('a').get('title')] = {
                    'Link': el.find('a').get('href')
                }

        await asyncio.gather(*tasks)
    print(auto_logos)


def sync_parsing():
    ...


def main():
    # url = 'https://www.drom.ru/catalog/'
    # save_page(url)
    # for i in range(1, 5):
    #     url = f'https://автолого.рф/car-logos/page/{i}/'
    #     save_page(url, f'car_logos_page{i}.html')

    asyncio.run(async_parsing())

    # with open('list_links_auto.txt', 'r') as file:
    #     source = file.read()
    # soup = BeautifulSoup(source, 'lxml')
    #
    # for mark in soup.find_all('a')[:5]:
    #     print(mark.text + ' -- ' + mark.get('href'))
    #     Path(f'AutoCatalog/{mark.text}').mkdir(parents=True, exist_ok=True)
    #     save_page(mark.get('href'), f'AutoCatalog/{mark.text}.html')
    #     auto_catalog[mark.text] = {
    #         'Link': mark.get('href'),
    #         'Models': {}
    #     }


    # with open('AutoCatalog/Acura.html', 'r') as file:
    #     source = file.read()
    # soup = BeautifulSoup(source, 'lxml')
    #
    # print(soup.find(class_=re.compile(r'css-ofm6mg exkrjba0')).find_all('a'))


if __name__ == '__main__':
    main()
