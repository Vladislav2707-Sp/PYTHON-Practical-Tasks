def convert_to_usd(amount_uah, rate = 41.5):
    total_usd = amount_uah / rate
    return f"Ви отримаєте \'{round(total_usd, 2)}\'"

# Стандартний курс
print(convert_to_usd(amount_uah= float(input("Введіть суму в гривнях: "))))
print()

# власний курс
print(convert_to_usd(amount_uah= float(input("Введіть суму в гривнях: ")), rate = float(input("Введіть курс USD: "))))