from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

with open('ГПИБ _ Газеты.html', 'r', encoding='utf8') as f:
    src = f.read()
# print(src)
soup = BeautifulSoup(src, 'lxml')

# list_papers = soup.find(class_='nodes-grid').find_all('li')
# print(list_papers[0])
# print(list_papers[0].get('data-id'))
# print(pd.DataFrame(list_papers))
#
list_papers = soup.find(class_='nodes-grid').find_all('li')
# print(list_papers)
# print(list_papers[0].find(class_='name').find('a').text)

dict_links = {el.get('data-id'): [el.find(class_='name').find('a').text,
              el.find('a')['href']] for el in list_papers}
print(pd.DataFrame.from_dict(dict_links, orient='index', columns=['Name', 'Link']))
