
def get_base_price(size): # ціна за розмір
    prices = {"S" : 120 , "M" : 180 , "L" : 240}
    return prices[size]

def calculate_toppings(toppings_list): #ціна за додаткові інградієнти
    toppings_price = 25
    total_toppings = len(toppings_list) * toppings_price
    return total_toppings 


def calculate_total(size, toppings_list, promo_code=None): # остаточна ціна
    total_size = get_base_price(size)
    total_topping_list = calculate_toppings(toppings_list)

    the_end_total = total_size + total_topping_list

    if promo_code == "STUDENT":
        the_end_total *= 0.9

    return the_end_total


#вибір розміру
size_pizza = input("Виберіть розмір піцци: \"S\", \"M\"або \"L\": ").strip().upper()


# вибір додаткових інгр.
toppings_list_input = list(map(str, input("введіть додаткові інградієнти: ").split()))



# фінальна ціна
final_total = calculate_total(size_pizza, toppings_list_input, promo_code = input("Введіть промокод: "))


print(f"Фінальна ціна вашого замовлення: {final_total}")