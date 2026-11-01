contact = {"name" : "Vladislav", "phone" : "+380992947103" , "city" : "Dnipro"}

email = input("Введіть пошту: ")
contact.setdefault("email", email)


print(contact.get("telegram", "Не вказано!") )

if "city" in contact:
    del contact["city"]


print(contact)