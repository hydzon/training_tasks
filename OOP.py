class Cat():
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age

    @property
    def breed(self):
        return self.breed

    @property
    def color(self):
        return self.color

    @property
    def age(self):
        return self.age

    @breed.setter
    def breed(self, value):
        self.breed = value

    @color.setter
    def color(self, value):
        self.color = value

    @age.setter
    def age(self, value):
        if value > self.age:
            self.age = value
        else:
            print("Кошка не может стать моложе")
        return self.age

    def meow(self):
        print('Мяу!')

    def purr(self):
        print('Мрррр')




class HomeCat(Cat):
    def __init__(self, breed, color, age, owner, name):
        super().__init__(breed, color, age)
        self.owner = owner
        self.name = name

    @property
    def owner(self):
        return self.owner

    @property
    def name(self):
        return self.name

    def getTreat(self):
        print("Мяяяяяяуууууу")

    @owner.setter
    def owner(self, value):
        self._owner = value

    @name.setter
    def name(self, value):
        self._name = value


# cat1 = Cat("Британец", "бежевый", 1)
cat1 = Cat("Британец", "бежевый", 1)
cat1.age = 2

cat2 = HomeCat("Мейкун", "серый", 3, "Михаил", "Бука")

print(cat1)
print(cat2)

