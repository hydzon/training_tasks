"""
Найти наиболее часто встречающееся слово в заданной строке.

"""

string = "Меня зовут Александр и мне 25 лет. Я занимаюсь программированием уже 5 лет и мне это нравится."

worlds = string.split()

d = {}
for word in worlds:
    if d.get(word):
        d[word] += 1
    else:
        d.update({word: 1})

max_c = 0
i = ()
for el in d.items():
    if el[1] > max_c:
        max_c = el[1]
        i = el

print(d)
print(i)
