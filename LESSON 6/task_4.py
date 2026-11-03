class Warrior:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def hit(self, enemy):

        if self.is_alive() == False:
            print(f"{self.name} не може атакувати, бо мертвий!")
            return

        if enemy.is_alive() == False:
            print(f"{enemy.name} вже програв!")
            print()
            return 

        enemy.health -= self.attack_power

        if enemy.health < 0:
            enemy.health = 0

        print(f"{self.name} атакує {enemy.name} і наносить {self.attack_power} урона")

        print(f"Здоров'я {enemy.name} : {enemy.health}")
        print()

        if enemy.is_alive() == False:
            print(f"{enemy.name} зазнав поразки!")




warrior_1 = Warrior(input("Введіть ім'я героя: "), float(input("Введіть к-сть здоров'я: ")), float(input("Введіть силу атаки: ")))
print()

warrior_2 = Warrior(input("Введіть ім'я героя: "), float(input("Введіть к-сть здоров'я: ")), float(input("Введіть силу атаки: ")))
print()


warrior_1.hit(warrior_2)
warrior_2.hit(warrior_1)
warrior_1.hit(warrior_2)