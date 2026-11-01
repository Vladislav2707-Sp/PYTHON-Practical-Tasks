n = int(input("Введіть число: "))

total = 0
count_1 = 0
count_2 = 0


for i in range(1, n + 1):
    total += i

    if i % 2 == 0:
        count_1 += i

    if i % 3 == 0:
        count_2 += 1



print(f"Сума всіх чисел від 1 до n: {total}")
print(f"Сума парних чисел: {count_1}")
print(f"К-сть чисел, які діляться на 3 без залишку: {count_2}")