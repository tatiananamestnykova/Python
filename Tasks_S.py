# Задача_1
# Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
# Для числа π в стране Малевии используют значение 3.14.
#
# Формат ввода, который используют Малевийцы:
#
# треугольник
# a
# b
# c
# где a, b и c — длины сторон треугольника
#
# прямоугольник
# a
# b
# где a и b — длины сторон прямоугольника
#
# круг
# r
# где r — радиус окружности

# Решение

# f = str(input())
# if f == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a+b+c)/2
#     s = (p*(p-a)*(p-b)*(p-c))**0.5
#     print(s)
# elif f == 'прямоугольник':
#     a = int(input())
#     b= int(input())
#     s = a * b
#     print(s)
# elif f == 'круг':
#     r = int(input())
#     s = 3.14 * r**2
#     print(s)

# Задача_2
# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки
# сначала максимальное, потом минимальное, после чего оставшееся число.
import math
# m = int(input())
# n = int(input())
# k = int(input())
# s = m+n+k
# print(max(m,n,k))
# print(min(m,n,k))
# print(s-max(m,n,k) - min(m,n,k))

# Задача 3
# a = int(input())
# if a%10==1 and a%100!= 11:
#     print(a, 'программист')
# elif a%10==2 and a%100!=12 or a%10==3 and a%100!=13 or a%10==4 and a%100!=14:
#     print(a, 'программиста')
# else:
#     print(a, 'программистов')

# Задача 4
# s = str(input())
# sum1 = int(s[0])+int(s[1])+int(s[2])
# sum2 = int(s[3])+int(s[4])+int(s[5])
# if sum1 == sum2:
#   print('Счастливый')
# else:
#   print('Обычный')
# Задача 5
# c = int(input())
# s = 0
# while c != 0:
#     s = s + c
#     c = int(input())
# print(s)

# Задача 6
# a = int(input())
# b = int(input())
# n = 1
# m = 2
# while n<m:
#   if n % a == 0 and n % b == 0:
#     n = m
#   else:
#     n = n+1
#     m = n+1
# print(n)

# Задача 7
# a = 0
# while a<=100:
#   a = int (input())
#   if a > 100:
#     break
#   if a<10:
#     continue
#   print(a)
# Задача 8
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     print('*', end='')
#   print()
# Задача 9
# a = int(input())
# b = int(input())
# s = 0
# c = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         s = s + i
#         c = c + 1
#         i = i + 1
# print(s / c)



