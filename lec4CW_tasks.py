# def func(x):
#     return x * x

# a = func
# print (a(5))
# print (func(5))

# def calc1(a, b):
#     return a + b

# def calc2(a, b):
#     return a * b

# def math (r, z, y):
#     print (r(z, y))

# # print (calc1(5, 25))
# # print (calc2(5, 25))
# # math (calc1, 5, 25)
# # math (calc2, 5, 25)

# math (lambda a, b: a + b, 5, 45)

# Задача 1
# выбрать четные числа и составить список из их пар (число, квадрат числа)
# 1 2 3 5 8 15 23 38
# Получить (2, 4), (8, 64), (38, 1444)

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# result = list()

# for i in list1:
#     if i % 2 == 0:
#         result.append((i, i ** 2))
# print (*result)

# Вариант с лямбда функцией

# def select(func, col):
#     return [func(x) for x in col]

# def chet(func, col):
#     return [x for x in col if func(x)] 

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# # result = select(int, list1)
# # print (result)
# # result = chet(lambda x: x % 2 == 0, result)
# # print (result)

# # result = list(select (lambda x: (x, x** 2), result))
# # print (result)

# # Задача 2

# # list1 = [x for x in range(1, 20)]
# # print (list1)

# # list1 = list(map(lambda x: x + 10, list1))
# # print (list1)

# # Задача 3
# # С клавиатуры вводиться некий набор чисел, в качестве разделителя используется пробел. Набор в качестве строки. Надо превратить список строк в список чисел

# # data = '12, 23, 15, 5, 8, 10'
# # print (data)

# # data = data.split()
# # print (data)

# # data = list(map(int, data.split()))
# # print(data)

# # функция filter
# # data = [15, 25, 34, 125, 65, 54, 32, 12]
# # res = list(filter(lambda x: x % 10 == 5, data))
# # print (res)

# # функция zip
# # numbers = [2, 9, 18, 28]
# # names = ["Дима", "Марина", "Андрей", "Никита"]

# # values = zip(names, numbers)
# # list = list(values)

# # print(list)

# # for i in range(5): # просто выводятся число от 0 до 4

# #     print(i)

# # for new_num in range(5, 10): # выодятся от 5 до 9

# #     print(new_num)

# # for temp in range(1, 11, 2): # с шагом 2

# #     print(temp)

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать data.writelines(colors) # разделителей не будет
# data.close()

# with open('file.txt', 'w') as data: 
#     data.write('line 1\n') 
#     data.write('line 2\n')

# path = 'file.txt' 
# data = open(path, 'r') 
# for line in data:
#     print(line) 
# data.close()

# import os
# print(os.path.abspath('main.py'))
# # 'C:/Users/79190/PycharmProjects/webproject/main.py'

# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) # 'main.py'

# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

# import os os.chdir('C:/Users/79190/PycharmProjects/GB')