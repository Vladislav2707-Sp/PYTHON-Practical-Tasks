pin = "1234"

count = 3


while count > 0:
    password = input("Password: ")
    
    if password == pin:
        print("Доступ надано!")
        break
    else:
        count -= 1

        if count > 0:
            print(f"Невірно. Залишилось спроб: {count}")
        else:
            print("Картку заблоковано!")