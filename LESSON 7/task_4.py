class Wallet:
    def __init__(self, balance = 0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance



class CryptoWallet(Wallet):
    def __init__(self, crypto_name, private_key, balance= 0):
        super().__init__(balance)
        self.crypto_name = crypto_name
        self.__private_key = private_key

    def transfer(self, amount, recipient_addres, key):
        self.amount = amount
        self.recipient_addres = recipient_addres
        self.key = key

        if self.key != self.__private_key:
            print(f"Неправильно введений ключ!")
        elif amount <= 0:
            print(f"Помилка! Сума переказу повина бути більшою за 0!")
        elif amount > self._balance:
            print(f"Недостатньо коштів на балансі !")
        else:
            self._balance -= amount
            print(f"Успішно знято {amount}! | адрес отримувача {recipient_addres} |  | Ваш баланс: {self._balance}")


my_crypto_wallet = CryptoWallet(input("Введіть назву монети: "), input("введіть приватний ключ: "), float(input("Ваш баланс: ")))
print()

print(f"Ваш баланс: {my_crypto_wallet._balance} {my_crypto_wallet.crypto_name}")
print()


#Перевірка, що сума депозита більша за 0
while True:
    deposit_input = float(input("Введіть суму депозита: "))
    if deposit_input <= 0:
        print("Сума депозита має бути більшою за 0!")
        print()
        continue
    else:
        print(f"Поповнення успішне! Додано: {deposit_input} | Ваш баланс: {my_crypto_wallet._balance + deposit_input} {my_crypto_wallet.crypto_name}")
        break

my_crypto_wallet.deposit(deposit_input)
print()



# Перевірка , що сума перевода більша за 0
# while True:
#     transfer_input = float(input("Введіть суму переказу: "))
#     if transfer_input <= 0 and transfer_input > my_crypto_wallet.balance:
#         print(f"Сума переказу повинна бути більшою за 0!")
#         print()
#         continue
#     else:
#         print(f"Успішно знято {transfer_input}!")
#         break




my_crypto_wallet.transfer(float(input("Введіть суму для переказу: ")), input("Введіть адрес для переказу: "), input("Введіть ключ: "))
print()


print(f"Баланс після всіх операцій становить: {my_crypto_wallet.get_balance()} {my_crypto_wallet.crypto_name}")