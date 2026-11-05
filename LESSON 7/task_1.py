class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def info(self):
        print(f"Транспорт: {self.brand}, швидкість: {self.speed} км/год")




class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery_capacity):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity

    def info(self):
        super().info()
        print(f"Ємність батареї: {self.battery_capacity} кВт·год")


car = ElectricCar("Mazda", 200, 75)
car.info()
