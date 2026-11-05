class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_permissions(self):
        return ["read", "comment"]


class Moderator(User):
    def get_permissions(self):
        return ["read", "comment", "delete_post"]


class Admin(User):
    def get_permissions(self):
        return ["all_access"]


user = User(input("Введіть ваше ім'я: "), input("Введіть вашу пошту: "))
print()

moderator = Moderator(input("Введіть ваше ім'я: "), input("Введіть вашу пошту: "))
print()

admin = Admin(input("Введіть ваше ім'я: "), input("Введіть вашу пошту: "))
print()


admin_stuff = [user, moderator, admin]


for i in admin_stuff:
    print(f"Користувач: {i.username.upper()} | Пошта: {i.email.upper()} | Права: {i.get_permissions()}", sep = "\n")
    print("-" * 70)