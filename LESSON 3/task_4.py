h = int(input("Введіть висоту фігури: "))

for x in range(1 , h+1):
    for y in range(x):
        print("*" , end = " ")
    print()