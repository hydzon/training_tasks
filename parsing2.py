'''
    Парсинг сайта health-diet.ru
'''
import datetime

from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import csv
import json
import os
import datetime, time

'''
    Сохраняем страницу
'''

# url_category = 'https://health-diet.ru/table_calorie/'
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'
# }
# req = requests.get(url_category, headers=headers)
# source = req.text
# with open('health-diet_category.html', 'w', encoding='utf-8') as f:
#     f.write(source)

'''
    Парсим категории и сохраняем в json
'''

# with open('health-diet_category.html', 'r', encoding='utf-8') as f:
#     soup = BeautifulSoup(f.read(), 'lxml')
# #
# print(soup.find_all('a', class_="mzr-tc-group-item-href"))
# dict_categories = {el.text: 'https://health-diet.ru' + el['href']
#                    for el in soup.find_all('a', class_="mzr-tc-group-item-href")}
# print(*dict_categories.items(), sep='\n')
# with open('health-diet_category.json', 'w', encoding='utf-8') as f:
#     json.dump(dict_categories, f, indent=4, ensure_ascii=False)

'''
    Пробегаемся по категориям и скачиваем страницы 
'''

# with open('health-diet_category.json', 'r') as f:
#     all_categories = json.load(f)
#
# for name_category, link in all_categories.items():
#     name_category = name_category.replace(' ', '_')
#     name_category = name_category.replace(',', '_')
#     name_category = name_category.replace('-', '_')
#     url_category = link
#     headers = {
#         'Accept': '*/*',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'
#     }
#     req = requests.get(url_category, headers=headers)
#     with open('category_pages/' + name_category + '.html', 'w', encoding='utf-8') as f:
#         f.write(req.text)

'''
    Парсим скачанные файлы и сохраняем в json
'''

# dict_products = {}
# directory = "category_pages"
# headers = ['Продукт', 'Калорийность', 'Белки', 'Жиры', 'Углеводы']
# id = 0
# for index, file_name in enumerate(os.listdir(directory)):
#     with open(f'{directory}/{file_name}', 'r', encoding='utf-8') as f:
#         soup = BeautifulSoup(f.read(), 'lxml')
#     # if index == 8:
#     #     break
#     # print(*soup.find(class_='uk-overflow-container').find('td').stripped_strings)
#
#     if soup.find(class_='uk-overflow-container'):
#         for el in soup.find(class_='uk-overflow-container').find('tbody').find_all('tr'):
#             current_el = list(zip(headers, list(el.stripped_strings)))
#             current_el.append(('Категория', file_name[:-5]))
#             dict_products[id] = {el[0]: el[1] for el in current_el}
#             id += 1
#
# with open(f'products.json', 'w', encoding='utf-8') as f:
#     json.dump(dict_products, f, ensure_ascii=False, indent=4)
# # data_frame = pd.DataFrame.from_dict(dict_products, orient='index', columns=headers + ['Категория'])
# # print(data_frame.groupby('Категория')[['Продукт']].count())

'''
    Работаем с данными
'''

with open('products.json', 'r', encoding='utf-8') as f:
    all_products = json.load(f)

data_frame = pd.DataFrame.from_dict(all_products,
                                    orient='index',
                                    columns=['Продукт', 'Калорийность', 'Белки', 'Жиры', 'Углеводы', 'Категория'])

print(data_frame.groupby('Категория')[['Продукт']].count())
