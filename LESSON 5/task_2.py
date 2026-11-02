def is_password_valid(password):
    if len(password) < 8:
        return False

    for i in password:
        if i.isdigit():
            return True

    return False

password_valid = is_password_valid(password = input("Ввдеіть пароль: "))
print()

if password_valid == True:
    print(f"Парль надійний!")
else:
    print(f"Парль занадто слабкий!")


