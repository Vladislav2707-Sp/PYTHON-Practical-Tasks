class BankAccont():
    def __init__(self, owner, balance = 0.0):
        self.owner = owner 
        self.balance = balance


#депозит
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"Ви поповнили рахунок на {amount} грн!", f"Ваш поточний баланс становить: {self.amount} грн.")
        print()

# print("Сума поповнення повинна бути більшою за 0!")


#зняття коштів
    def withdraw(self, amount):
        self.amount = amount
        # if amount < 0:
        #     print("Сума зняття повинна бути більшою за 0!")

        total_deposit = self.balance - self.amount
        print()

        if self.amount < self.balance:
            print(f"Ви зняли {self.amount} грн. Ваш баланс: {total_deposit} грн.")
        else:
            print("Недостатньо коштів на рахунку!")
            return False



bank = BankAccont("Vladislav")


while True:
    deposit_input = float(input("Введіть суму депозиту: "))
    if deposit_input < 0:
        print("Сума поповнення повинна бути більшою за 0!")
        print()
        continue
    else:
        break

bank.deposit(deposit_input)


while True:
    withdraw_input = float(input("Введіть суму для зняття: "))
    if withdraw_input < 0:
        print('Сума зняття повинна бути більшою за 0!')
        print()
        continue
    if bank.withdraw(withdraw_input) == False:
        print("Спробуйте ще раз")
        print()
        continue
    else:
        break

bank.withdraw(withdraw_input)

