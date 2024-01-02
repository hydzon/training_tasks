import math

class Planet:

    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = round(4 * math.pi * radius**2)
        self.average_temp_celcius = temp_celsius
        self.average_temp_fahrenheit = temp_celsius * 9/5 + 32

    def show_info(self):
        print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
        print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit}° по Фаренгейту.")


jupiter = Planet('Юпитер', 69911, -108)
jupiter.show_info()


print()
"""==========================================================================================================="""
print()


class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name} ({self.phone})')

class Friend(User):
    def show(self):
        print(f'Имя: {self.name} || Телефон: {self.phone}')


def show_data(anything):
    anything.show()


father = User("Дюма-отец", "+33 3 23 96 23 30")
son = Friend("Дюма-сын", "+33 3 23 96 23 30")

show_data(son)
show_data(father)


print()
"""==========================================================================================================="""
print()

class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print("Очень интересный вопрос! Не знаю.")

class Student(Human):
    def ask_question(self, someone, question):
        print(f"{someone.name},  {question}")
        someone.answer_question(question)
        print()

class Curator(Human):
    def answer_question(self, question):
        if question == "мне грустненько, что делать?":
            print("Держись, всё получится. Хочешь видео с котиками?")
        else:
            super().answer_question(question)


# объявите и реализуйте классы CodeReviewer и Mentor
# следующий код менять не нужно, он работает, мы проверяли

student1 = Student('Тимофей')
curator = Curator('Марина')
# mentor = Mentor('Ира')
# reviewer = CodeReviewer('Евгений')
# friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
# student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(curator, 'когда каникулы?')
# student1.ask_question(reviewer, 'что не так с моим проектом?')
# student1.ask_question(friend, 'как устроиться на работу питонистом?')
# student1.ask_question(mentor, 'как устроиться работать питонистом?')