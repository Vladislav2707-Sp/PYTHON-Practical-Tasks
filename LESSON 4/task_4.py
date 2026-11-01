hero = {"potion": 3, "gold": 150, "sword": 1}
chest = {"gold": 50, "shield": 1, "arrows": 20}



hero["gold"] += chest["gold"]
chest.pop("gold")
hero.update(chest)

hero['potion'] -= 1

delete_object = hero.popitem()
print(f"Було вилучено \'{delete_object[0]}\' у кількості {delete_object[1]}")


for a,b in hero.items():
    print(f"{a} : {b}")