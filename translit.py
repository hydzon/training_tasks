'''
    Транслит русского слова в английское и обратно
    В соответствии с ГОСТ 7.79-2000
'''

dict_rus_eng = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
    'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': "'", 'Ы': "Y'", 'Ь': "'",
    'Э': "E'", 'Ю': 'Yu', 'Я': 'Ya', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': "'", 'ы': "y'", 'ь': "'", 'э': "e'", 'ю': 'yu', 'я': 'ya', ' ': ' '
}


lat = ('yo', 'zh', 'tc', 'ch', 'sh', 'sh', 'yu', 'ya', 'Yo', 'Zh', 'Tc', 'Ch', 'Sh', 'Shch', 'Yu', 'Ya', 'W')
rus = ('ё', 'ж', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', 'Ё', 'Ж', 'Ц', 'Ч', 'Ш', 'Щ', 'Ю', 'Я', 'В')
lat_eng = ("ABVGDEZIJKLMNOPRSTUFH_I_Eabvgdezijklmnoprstufh_i_e", "АБВГДЕЗИЙКЛМНОПРСТУФХЪЫЬЭабвгдезийклмнопрстуфхъыьэ")


def translit_ru_to_eng(word):
    return ''.join([dict_rus_eng[ch] for ch in word])


def translit_eng_to_ru(word):
    for lat_char in lat:
        if word.count(lat_char):
            word = word.replace(lat_char, rus[lat.index(lat_char)])
    for lat_char in lat_eng[0]:
        if word.count(lat_char):
            word = word.replace(lat_char, lat_eng[1][lat_eng[0].index(lat_char)])
    return word


def main():
    pass


if __name__ == '__main__':
    main()
