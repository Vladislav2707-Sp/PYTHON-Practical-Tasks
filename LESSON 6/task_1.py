class Phone:
    def __init__(self, model, battery):
        self.model = model
        self.battery = battery

    def __str__(self):
        return f"Телефон {self.model}, заряд: {self.battery}%"


iPhone = Phone("iPhone", 85)
Samsung = Phone("Samsung" , 40)

print(iPhone)
print(Samsung)