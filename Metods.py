class CoffeeShop:
    specialty = 'espresso'

    def __init__(self, coffee_price):
        self.coffee_price = coffee_price

    # instance method
    def make_coffee(self):
        print(f'Making {self.specialty} for ${self.coffee_price}')

    # static method
    @staticmethod
    def check_weather():
        print('Its sunny')

    def change(self, spc):
        self.specialty = spc
        print(f'Specialty changed to {spc} for only ${self.coffee_price}')

    # class method
    @classmethod
    def change_specialty(cls, specialty):
        cls.specialty = specialty
        print(f'Specialty changed_specialty to {specialty}')


coffe1 = CoffeeShop("10")
coffe1.make_coffee()
coffe2 = CoffeeShop("3")
coffe2.make_coffee()
coffe3 = CoffeeShop("90")
coffe3.make_coffee()
print()

coffe1.change_specialty("EASY")
coffe1.make_coffee()
coffe2.make_coffee()
coffe3.make_coffee()
print()

coffe2.change("HARD")
coffe1.make_coffee()
coffe2.make_coffee()
print()

coffe1.change_specialty("EASY")
coffe1.make_coffee()
coffe2.make_coffee()
print()

coffe2.change("MEDIUM")
coffe1.make_coffee()
coffe2.make_coffee()
print()

coffe1.change_specialty("NEW")
coffe1.make_coffee()
coffe2.make_coffee()
coffe3.make_coffee()
print()

print(id(coffe1))
print(id(coffe2))



