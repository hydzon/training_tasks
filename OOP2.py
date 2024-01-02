class Contact:
    def __init__(self, name, phone, address, birthday):
        self._name = name
        self._phone = phone
        self._address = address
        self._birthday = birthday

    def __str__(self):
        return f"Name: {self.name},  Phone: {self.phone},  Adr: {self._address},  DR: {self._birthday}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def print_contact(self):
        print(f"Name: {self.name},  Phone: {self.phone},  Adr: {self._address},  DR: {self._birthday}")






leo = Contact("Лев Толстой", "+7 (123) 456-78-90", "Ясная Поляна", "9.09.1828")
mike = Contact("Михаил Булгаков", "2-03-27", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6", "15.05.1891")
vlad = Contact("Владимир Маяковский", "73-88", "Россия, Москва, Лубянский проезд, д. 3, кв. 12", "19.07.1893")

mike.print_contact()
mike.address = "Россия, Москва, Нащокинский переулок, дом 3, кв. 44"
mike.phone = "К-058-67"
mike.print_contact()

print(mike)
