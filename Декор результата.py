"""
Напишите декоратор answer, который преобразует функцию, принимающую неограниченное число позиционных и именованных
параметров и возвращает её результат с припиской "Результат функции: <значение>".

"""

def decor(func):
    def wraper(*args, **kwargs):
        print("Результат функции: " + func(*args, **kwargs))
    return wraper


@decor
def foo(*args, **kwargs):
    return "3"


foo()
