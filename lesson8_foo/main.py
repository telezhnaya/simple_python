from math import *

print()  # Выведется пустая строчка
print("Hello world!")  # Классика :)
print("hello", 1, 2, "Olya")  # Сколько угодно всего, через запятую

print("Abs test", abs(-5.75))  # abs принимает и возвращает ровно одно число
# Тут получили бы ошибку
# a = abs()
# a = abs(10, 20)
# a = abs("hello")
# a = abs("125")


print("len of list test", len([1, 10, 100]))  # Уже нам знакомая len
print("len of str test", len("hello"))  # Может также измерять длину строки


a = abs(5)  # получим int
a = abs(7.5)  # а тут - float
a = print()  # обсудим в следующий раз :)

# a = input()  # тут будет строка, вне зависимости от того, что мы введем
# a = int(input())  # А тут мы преобразуем это к числу.

print("type test")
print(type(5.99), type(int(5.99)), type(str(5.99)))
a = "4.75"
print(type(a), type(float(a)))
# print(type(int(a)))  # Получим ошибку. Надо в 2 шага:
print(type(int(float(a))))

# Воспринимайте место вызова функции так, будто там находится ее результат
# abs возвращает число - читайте код, представляя вместо abs(x) обычное число
a = abs(-17) * 10 - abs(-4.6)
print("Мы тут насчитали", a)
