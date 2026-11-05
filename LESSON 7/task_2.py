class ATMcard:
    def __init__(self, card_holder, pin="1234"):
        self.card_holder = card_holder
        self.__pin = pin



    def verify_pin(self, pin_input):
        if pin_input == self.__pin:
            print("Пароль введено вірно!")
            return True
        else:
            print("Пароль введено невірно!")
            return False



    def change_pin(self, old_pin, new_pin):

        if self.verify_pin(old_pin):
            if len(new_pin) == 4 and new_pin.isdigit():
                self.__pin = new_pin
                print(f"Шановний {self.card_holder} , PIN успішно змінено!")
            else:
                print("Помилка! Новий PIN повинен містити рівно 4 цифри!")
        else:
            print("Пароль введено невірно!")




password = ATMcard(input("Введіть ім'я: "))

password.verify_pin(input("Введіть PIN: "))
print()


password.change_pin(input("Введіть старий PIN: "),input("Введіть новий PIN: "))
print()

password.verify_pin(input("Перевірка нового PIN: "))