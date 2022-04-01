# lst = [5,6,7,6,8,6,48, 70, 67, 55]
# a=0
# for i in lst:
#     if i%2==0:
#         a=i+a
# print(a)

# задача три отсортировать список чисел: чётные, потом нечётные
# lst = []
# x = list(range(0, 100, 2))
# y = list(range(1, 100, 2))
# x.append(y)
# print(x)

# lst = [5, 8, 12, 9, 45, 23, 44, 65, 88, 5, 2]
# for i in lst:
#     if i%2!=0:
#         lst.append(i)
# print(lst)
#
# # lst = [2, 'hello', 5, 6, 'world']
# a = []
# b = []
# for i in lst:
#     if type(i) is str:
#         a.append(i)
#     elif type(i) is int or type(i) is float:
#         b.append(i)
# print(a)
# print(b)
# elif isinstalse(i, (int, float))

# from random import randint
# numbers = [1, 2, 3, 4, 6]
# i = 0
# while i<len(numbers)-1:
#     el = numbers[i]
#     if el%2==0:
#         i+=1
#     else:
#         numbers.append(el)
#         numbers.remove(el)
# print(numbers)

# 4 задача:
# lst = [2, 'hello', True]
# i = 0
# while i<len(lst):
#     if type(lst[i]) is str:
#         del lst[i]
#     else:
#         i+=1
# print(i)

# message = 'python'
# key = 'stdghj'
# #print("".join(format(orld("l"), "b")))

# В строке определить количество пар одинаковых
# символов рядом стояoих в строке, пример Hello 1 параб АааИИИ 2 пары
# str = "ffkklldjf"
# couter = 0
# i = 0
# while i<len(str)-1:
#     if str[i]==str[i+1]:
#         couter+=1
#         i+=2
#     else:
#         i+=1
# print(couter)

# чётные в конец списка
# lst = [1, 5, 6, 5, 7, 8, 4]
# for i in range(len(lst)):
#     if lst[i]%2==0:
#         lst.insert(0, lst.pop(i))
# print(lst)

# Дана строка, некоторый текс в ней написан в скобках, удалить все скобки и х содержимое
# text = 'текс текст (два текста) текст текст (третий текст)'
# while '(' in text and ")" in text:
#     left = text.find("(")
#     right = text.find(")")
# #   text = text[:left] + text[right+2:]
# # print(text)
# #
# # через replace
#     part = text[left:right+2]
#     text = text.replace(part, "")
# print(text)

# дан текст, символам @ помечен backspase (пра@ив@ва@ет)
#необходимо удалить все собачки и символ перед нимб восстановить строку
# text = "пра@ив@ва@ет"
# clear_text= ""
# for i in range(len(text)-1):
#     if text[i]!="@" and text[i+1] != "@":
#         clear_text+=text[i]
#     if text[-1]!="@":
#         clear_text+=te[-1]
# print(clear_text)
# или
# while "@" in text:
#     a = text.find("@")
#     b = text[a-1:a+1]
#     text = text.replace(b, "")
# print(text)
#Подготовка к экзамену:
# text='gwertgwertawert'
# print(text.count("w", 3, 7))
# a = "1"*int('5')
# print(a)
# a = 2*3
# a = "1"*5
# print(a)
# b = "1"-"2"
# print(b)
#c = "spрорam"[::-3]
#print(c)

#
# 'a'+'x'
# if '123'.isdigit():
# else:
#     'y'+"b"

# i=0
# while i<10:
#     i+=1
# i-=10
# print(i)

# for i in range(1, 10):
#     i-=5
#     print(i)
