sentence_no_exercise = list(map(str , input("Введіть речення: ").split()))
# print(len(sentence.strip()))

print("Не є завданням!")
count_letter = 0

for i in sentence_no_exercise:
    total = len(i)
    count_letter += total
print(f"К-сть всих символів окрім пробілів: " , count_letter)





sentence = input("Введіть речення: ")
my_dict = {}

print("______________________________________")
print("")

for i in sentence:
    if i == " ":
        continue
    
    my_dict[i] = my_dict.get(i, 0) + 1

print(my_dict)



max_letter = ""
count_letter = 0

for i in my_dict:
    if my_dict[i] > count_letter:
        count_letter = my_dict[i]
        max_letter = i

print(f"У тексті найчастіше зустрічається символ \'{max_letter}\' , а саме {count_letter} разів.")





max_return = my_dict.setdefault(i , max(my_dict.values()))
# print("У тексті найчастіше зустрічається символ \'{max_retun}\'")