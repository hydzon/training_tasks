"""
Напишите функцию, которая по заданным коэффициентам строит строку, описывающую валидное с точки зрения Python выражение
без использования оператора возведения в степень.

"""

def make_equation(*args):
    if len(args) > 1:
        return f"({make_equation(*args[:-1])}) * x + {str(args[-1])}"
    return f"({args[0]})"


result = make_equation(3, 2, 1)
print(result)
