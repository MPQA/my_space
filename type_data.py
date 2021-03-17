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
fio = "Pastovenskyi Wladinirovich"
print (name, fio)
print (line)

#bool
status1 = True
status2 = False
print (status1, status2)
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
print (type (status1))
print (type (a1))
print (type (x))
print (line)

x=y=z=888
print (x)
print (y)
print (z)
print (line)

q1 = 10
q2 = 2+4
q3 = 44
q4 = 2.5

w = q1 * q4
w1 = q3 / q1
print (w,'\n',w1)
print (line)

#\n новая строка
text = 'The GLOCK G18C -\ncomes with compensator slots in the barrel and slide.'
print (text)
print (line)


print("Hello\rWorld!")
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



x1,x2,x3,x4 = 1,4,16,21
print (x1,x2,x3,x4)

x1,x2,x3,x4 = 2,5,17,22
print (x1,x2,x3,x4)

print (line)

line = '------------------------[xxx]'
print (line)

#множественное присваивание
x1,x2,x3,x4 = 1,4,16,21
print (x1,x2,x3,x4)
print (line)

# умноження
c1=x2*x3
print (line)
# деление
c2=x4/x2
type (c2)
print (line)
# присвоение другого типа данных
c3 = int(c2)
print (x1,x2,x3,x4,c1,c2,c3)
print (line)


yy1 = 21 / 5
yy2 = 1999 / 1000
print ('yy1=', yy1, 'yy2=', yy2)

y1 = 21 // 5
y2 = 1999 // 1000
print ('y1=', y1, 'y2=', y2)

y3 = 21%5
y4 = 1999 % 1000
print ('y3=', y3, 'y4=', y4)
print (line)

type (y1)





# преобразование с string в int через float
# напрямую от string в int не получится
# напоминую string для всего насвете, а float для
s = '123.999'
print (s)
print (type (s))

x = float (s)
print (x)
print (type (x))

y = int (x)
print (y)
print (type (y))

t = round(149.4999)

bin(t)
print (t)

#в переменную name укладываем значение с input
# name = input()
# print ('ничоси у тебя имя ' + name)


a = int('19') # Переводим строку в число
#b = int('19.5')  # Строка не является целым числом
c = int(19.5)  # Применённая к числу с плавающей точкой, отсекает дробную часть
print (a, c)

d = bin(19) # bin(x) - преобразование целого числа в двоичную строку.
print (d)
i = oct(19) # oct(х) - преобразование целого числа в восьмеричную строку.
print (i)
f = hex(19) # hex(х) - преобразование целого числа в шестнадцатеричную строку.
print (f)
0b10011  # Так тоже можно записывать числовые константы
