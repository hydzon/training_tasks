"""
1)  У частных легковых автомобилях номера — это буква, три цифры, две буквы, затем две или три цифры с кодом региона.
    У такси — две буквы, три цифры, затем две или три цифры с кодом региона.
    Определите тип номера. Буквы в номерах — заглавные русские. Маленькие и английские для простоты можно игнорировать.

2)
"""

# import numpy as np
# import pandas as pd
import re


# ============================================     tasks 1-5   =========================================================

def task1(string):
    if re.match(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', string):
        return 'Private'
    elif re.match(r'[АВЕКМНОРСТУХ]{2}\d{2}\d{2,3}', string):
        return 'Taxi'
    return 'Fail'


# ============================================     MAIN     ===========================================================

def main():
    '''

    '''

    # print(re.match(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', input()))

    # input_str = input()
    # while input_str:
    #     print(task1(input_str))
    #     input_str = input()

    '''
        Слово — это последовательность из букв (русских или английских), внутри которой могут быть дефисы.
        На вход даётся текст, посчитайте, сколько в нём слов.
    '''
    with open('input.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        print(len(re.findall(r'\b[\w^-]+\b', s)))


if __name__ == '__main__':
    main()
