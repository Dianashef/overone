# 8.2. Программа принимает список из трех слов. Создать словарь, в котором ключ — слово,
# значение — количество символов в слове

# a = input("Введите слова:").split()
# #print(a)
# dict = {i:len(i) for i in a}
# print(dict)

# 8.3 На вход подается список чисел. Создать словарь, в котором ключ — число, значение —
# число на 10% больше. Значение должно быть округленное

# a = input("Введите числа:").split()
# dict = {int(i):round(int(i) * 1.1, 2) for i in a}
# print(dict)

# 8.6 Создать словарь, который в качестве ключа будет использовать страну, а в качестве
# значения - ее столицу. Внеси в него следующие страны: Россия (Москва), Украина
# (Киев), Италия (Рим), Испания (Мадрид), Болгария (София).
# Программа должна запрашивать у пользователя, столицу какой страны он хочет узнать
# и выдавать результат.

# dict = {"Россия": "Москва", "Украина": "Киев", "Италия": "Рим", "Испания": "Мадрид", "Болгария": "София"}
# a = input("Введите столицу какой страны  хотите узнать:").lower()
# for key, value in dict.items():
#     key = key.lower()
#     if key == a:
#         print(value)

# 8.7 Создать словарь, ключи — числа, значения — слова. Удалить из него все
# пары с нечетными ключами. Вывести на печать
# В этом вам может помочь статья, что сбрасывала ранее

#dict = {1:"one", 2:"two", 3:'three', 4:"four", 5:"five", 6:"six", 7:"seven"}
# now_dict = {k: v for k, v in dict.items() if k%2==0}
# print(now_dict)

# или
# non_citric = {k: incomes[k] for k in dict.keys() - {'k%'}}

# for key in list(dict.keys()):
#     if key%2!=0:
#         del dict[key]
# print(dict)

# 10.2 Прочитать из файла числа, сформировать список и напечатать его
# Out: [10, 91, 76, 48, 11, 89, 65, 56, 81, 94, 36]

# with open('file.txt', 'r') as f:
#     text = f.read()
#     lst = text.split(' ')
#     #print(lst)
# lst_1 = [int(i) for i in lst]
# print(lst_1)

# 10.4 Прочитать предыдущий файл,сформировать из него словарь, распечатать его
# Out: {'1': 'Sun', '2': 'Mon', '3': 'Tue', '4': 'Wed', '5': 'Thu', '6': 'Fri', '7': 'Sat'}
d = {}
with open('file.txt', 'r') as f:
    for i in f:
        text = f.readline()
        text_1 = text.split(":")
        print(text_1)


# 10.8 Дан список [5, True, ‘abc’], # Записать его в файл

# list = [1, True, 'abc']
# with open('file_1.txt', 'w') as my_file:
#     for i in list:
#         my_file.write(str(i) + '\n')
#
# 10.9 Создать список чисел. Записать каждое нечетное число в файл

# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# with open('file_1.txt', 'w') as f:
#     for i in list_2:
#         if i%2!=0:
#             f.write(str(i) + '\n')

#10.7 Пользователь вводит слова. Записать их в файл: каждое слово на отдельной строке
# a = input("Введите слова:").split()
# with open('file_1.txt', 'w') as f:
#     for i in a:
#         f.write(i + '\n')