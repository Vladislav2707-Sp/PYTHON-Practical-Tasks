tasks = []

# ex2
task_1 = tasks.append(input("Введіть завдання: "))
task_2 = tasks.append(input("Введіть завдання: "))
task_3 = tasks.append(input("Введіть завдання: "))

#3 ex
for index, task in enumerate(tasks, 1):
    print(f"{index}.{task}")

# 4 ex
number = int(input("оберіть ноемр завдання для видалення: "))
delete_task = tasks.pop(number - 1)
print(f"Завдання \"{delete_task}\" виконано та видалено!")


# Ex 5
tasks.sort()
print(tasks)