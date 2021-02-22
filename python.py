#!/usr/bin/python
# -*- coding: utf-8 -*-

# int целые числа как + так и -
a = 30;
dog = 10;
book = 45;
line = '_________________'
print (a, dog, book)
print (line)

# float дробные числа
volume = 12.5
vodka = 0.75
salary = 1488.01
p = float(22)
print (volume, vodka, salary, p)

print (line)

#string # str
name = "Misha"
fio = "Misha Past Wladinir"
print (name, fio)
print (line)

#bool
status = True
status = False
print (status)
print (line)

#comlex
a1 = 44
f_1 = 100
print (a1, f_1)
print (line)

x = 'Hello World'
print (x)
print (line)

print (type (a))
print (type (vodka))
print (type (fio))
print (type (status))
print (type (a1))
print (type (x))

x=y=z=0
print (x)
print (y)
print (z)
print (line)

q1 = 10
q2 = 2+4
q3 = 44
q4 = 2.5

w = q1 * q4
w1 = q1 / q4
print ('w\n',w1)
print (line)

#/n новая строка
text = 'The GLOCK G18C -\ncomes with compensator slots in the barrel and slide.'
print (text)
print (line)

print(f"Hello\nWorld!")
print (line)
print(f"Hello\rWorld!")
print (line)

#множественное присваивание
x1,x2,x3,x4 = 1,2,5,8
c1=x2*x3
c2=x4/x2
print (x1,x2,x3,x4,c1,c2)
c3 = int(c2)

print (line)

tmp1 = x1
tmp2 = x2
x1 = tmp2
x2 = tmp1

print (x1,x2,x3,x4)
print (line)

r1 = x1+x3
r2 = x2+x4

print (r1,r2) #7і9
print (line)

#x1,x2 = x3,x4
print (x1,x2,x3,x4)
print (line)

x1,x2 = x2,x1
print (x1,x2)
print (line)

# в квадрате. поднести в степень
# ДВОЙНОЕ УМНОЖЕНИЕ ЭТО ВОЗВЕДЕНИЕ В СТЕПЕНЬ
e1 = 2**2 #в степень 2
e2 = 12**2
e3 = 9**0.5 # так ПОДНЕСТИ К КОРНЮ
print (e1, e2, e3)
