import random
# генераторы списков
# a = [i for i in range(10)]
# print(a)
# a = [random.randint (-10, 10) for i in range(10)]
# print(a)
# # a = [elem*2 for elem in a]
# print(a)
# b = [elem for elem in a if elem%2==0]
# print(b)




# a = input().split()
# a = [int(i) for i in a]
# print(a)

# n = 5
# m = 4
# a = [[0]*m for i in range(n)]
# print(a)
# for i in a:
#     print(i)

# a = [ (i, j) for i in 'abc' for j in [1,2,3]]
# print(a)

# a = [ i*j for i in [2, 3 , 4, 5] for j in [1,2,3] if i*j>10]
# print(a)

# ls = []
# for i in range(2):
#     text = input().split()
#     for elem in text:
#         if '@' in elem:
#             ls.append(elem)
#
# print(tuple(ls))
#7.3.На вход программа получает несколько чисел. Создать кортеж из чисел, кратных 3м.
# a = [random.randint (0, 100) for i in range(10)]
# b = [elem for elem in a if elem%3==0]
# b = tuple(b)
# print(b)

#Задача 7.3. На вход программа получает несколько чисел. Создать кортеж из чисел, кратных 3м.
# a = input('Введите число:').split()
# num2 = []
# for i in a:
#     i = int(i)
#     if i%3==0:
#         num2.append(i)
# print(tuple(num2))

#Задача 7.4.Создайте кортеж с числами от 0 до 9 и посчитайте сумму элементов.
# tpl = tuple(range(1, 10))
# print(sum(tpl))

# Задача 7.5.Создайте кортеж с буквами. Посчитайте сколько гласных  и выведите на экран в формате:
# «Буква а в кортеже встречается 1 раз»
# letter = tuple([str(i) for i in input("введите буквы ").split()])
# print(letter)
# letter_e= letter.count('e')
# letter_y = letter.count('y')
# letter_u = letter.count('u')
# letter_i = letter.count('i')
# letter_o = letter.count('o')
# letter_a = letter.count('a')
# print('Буква e в кортеже встречатся', letter_e, 'раз')
# print('Буква y в кортеже встречатся', letter_y, 'раз')
# print('Буква u в кортеже встречатся', letter_u, 'раз')
# print('Буква i в кортеже встречатся', letter_i, 'раз')
# print('Буква o в кортеже встречатся', letter_o, 'раз')
# print('Буква a в кортеже встречатся', letter_a, 'раз')

# задача HT_7_1. Создайте 2 кортежа с 10 случайными числами от -5 до 0. Объедините их и посчитайте
# сколько раз в получившемся кортеже встретится 0
# a = tuple([random.randint (-5, 0) for i in range(10)])
# print(a)
# b = tuple([random.randint (-5, 0) for i in range(10)])
# print(b)
# tlp = a+b
# print(tlp)
# print(tlp.count(0))

 #задача HT_7_2. Создайте кортеж из 5 случайных чисел от 1 до 10. Все числа, кроме первого и
# последнего, распаковать в один список. Для распаковки используйте *
# tpl = tuple([random.randint (1, 10) for i in range(5)])
# print(tpl)
# a, *ls, b = tpl
# print(ls)

#задача HT_7_3. На вход программе подаются числа. Создайте кортеж из чисел меньше 5.
# a = input('Введите числа:').split()
# num2 = []
# for i in a:
#     i = int(i)
#     if i< 5:
#         num2.append(i)
# print(tuple(num2))

#задача HT_7_4. У вас есть кортеж, который содержит список. Измените кортеж так, чтобы список был пустым.
# tlp = ('1', '2', '3', ['a', 'b', 'c'])
# *a, d = tlp
# d.clear()
# print(tlp)

#задача 9.1. На вход программа получает последовательность чисел, букв и иных символов. Преобразуйте их в множество
# a = input("Введите").split()
# print(set(a))

#Задача 9.2. На вход программа получает  список чисел, определите  сколько в нем уникальных чисел
# b = input("Введите").split()
# print(len(set(b)))

# задача 9.3.На вход прорамма получает  список чисел. Для каждого  числа, которое ранее встречалось, выведите слово
# YES, если число не встречалось, то NO
# a = input("Введите").split()
# b = set(a)
# for i in b:
#     if a.count(i)>1:
#         print(i, "YES")
#     else:
#         print(i, 'NO')

#Задача 9.4 На вход программа получает 2 набора чисел. Посчитайте сколько одинаковых чисел
# содержится в первом и втором наборах.
# set_1 = set(input("Введите").split())
# set_2 = set(input("Введите").split())
# set_3 = set_1 & set_2
# print(len(set_3))


#задача 9.5. На вход программа получает 2 набора чисел. Найдите одинаковые числа в этих наборах и выведите их в
#порядке возрастания.
# set_1 = set(input("Введите").split())
# set_2 = set(input("Введите").split())
# set_3 = sorted(set_1 & set_2)
# print(set_3)

# задача 9.6. На вход прорамма получает 2 строки и выводит только те элементы, которые есть в первой строке и отсуствуют
# во второй. Т.е. одинаковые элементы исключаются
# str = input("Введите")
# str_2 = input("Введите")
# set_1 = set(str)
# set_2 = set(str_2)
# set_3 = set_1-set_2
# print(set_3)

#задача 9.1. На вход программа принимает 2 строки и выводит их общие символы.
# str = input("Введите")
# str_2 = input("Введите")
# set_1 = set(str)
# set_2 = set(str_2)
# set_3 = set_1 & set_2
# lst = list(set_3)
# lst.remove(' ')
# print(lst)

#задача 9.2. На вход программа принимает 2 строки и выводит все символы из второй строки, которых нет в первой
# str = input("Введите")
# str_2 = input("Введите")
# set_1 = set(str)
# set_2 = set(str_2)
# set_3 = set_2 - set_1
# print(set_3)