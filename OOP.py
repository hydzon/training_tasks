"""
Абстракция
"""
class Predator:
    def hunt(self):
        print('Охотится...')

"""
Инкапсуляция
"""

class Cat(Predator):
    def __init__(self, breed, color, age):
        self._breed = breed
        self._color = color
        self._age = age

    @property
    def breed(self):
        return self._breed

    @property
    def color(self):
        return self._color

    @property
    def age(self):
        return self._age

    @breed.setter
    def breed(self, value):
        self._breed = value

    @color.setter
    def color(self, value):
        self._color = value

    @age.setter
    def age(self, value):
        if value > self._age:
            self._age = value
        else:
            print("Кошка не может стать моложе")
        return self._age

    def meow(self):
        print('Мяу!')

    def purr(self):
        print('Мрррр')

    def sleep(self):
        print('Свернулся в клубок и сладко спит.')

"""
Наследование
"""

class HomeCat(Cat):
    def __init__(self, breed, color, age, owner, name):
        super().__init__(breed, color, age)
        self._owner = owner
        self._name = name

    @property
    def owner(self):
        return self._owner

    @property
    def name(self):
        return self._name

    def getTreat(self):
        print("Мяяяяяяуууууу")

    @owner.setter
    def owner(self, value):
        self._owner = value

    @name.setter
    def name(self, value):
        self._name = value

"""
Полиморфизм
"""
class Parrot:
  def sleep(self):
    print('Сел на жёрдочку и уснул.')


def homeSleep(animals):
    animals.sleep()


# cat1 = Cat("Британец", "бежевый", 1)
cat1 = Cat("Британец", "бежевый", 1)
cat1.age = 2
cat2 = HomeCat("Мейкун", "серый", 3, "Михаил", "Бука")
pat = Parrot()


cat1.hunt()
print(cat1.breed)
print(id(cat1))
homeSleep(cat1)
homeSleep(pat)

cat2.hunt()
print(cat2.breed)
print(id(cat2))

