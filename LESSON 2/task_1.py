inventory = ["Ноутбук", "Мишка", "Клавіатура"]

inventory.append("Монітор")
inventory.insert(1, "Килимок")
print(f"Продано: {inventory.pop(0)}")
inventory.remove("Мишка")

print(inventory)