goods = {"Ноутбук": 28000, "Мишка": 650, "Клавіатура": 1800, "Монітор": 7500, "USB-флешка": 350}

# 1
print("Завдання №1")
for product, price in goods.items():
    print(f"Товар: {product} | Ціна: {price} грн")
print()
print()

# 2
print("Завдання №2")
middle_price = sum(goods.values()) / len(goods)
print("Середня вартість товару: ", middle_price, "грн.")
print()
print()

#3
print("Завдання №3")
for product, price in goods.items():
    if price < 1000:
        print(f"Товар: {product} | Ціна: {price}")