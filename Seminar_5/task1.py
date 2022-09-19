'''
Задана натуральная степень n. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени n.
Пример:
- n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 (коэф: []) или 10*x² = 0

Уточнения:
n - это степень икса первого элемента полинома
при n =3 => 5*x*3 + 18*x**2 + 7*x + 19 = 0 - коэффициенты = [5,18,7,19]
при n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
при n=10 => 56 * x*10 = 0

коэффициенты - это числа перед элементами полинома.
коэффициенты могут быть нулем, кроме первого
'''

import random

n = random.randint(1, 10)
print(f"Натуральная степень {n}")
list_num = [random.randint(1, 100)]
for i in range(1, n + 1):
    list_num.append(random.randint(0, 100))
print(f"Список коэффициентов: {list_num}")
list_x = []
for i in range(n + 1):
    list_x.insert(0, 'x**' + str(i))
print(list_x)
polinom = list(zip(list_num, list_x))
print(polinom)

# s = str('')
# for i in range(n):
#     if i == 0:
#         s += str(polinom[i])
#     elif i == 1:
#         s += '+' + str(polinom[i]) + 'x'
#     else:
#         s += str(polinom[i]) + 'x**' + str(i)

# print(f'\n{s}')

s = str("")
for i, element in enumerate(polinom):
    for j in element:
        s = s + str(j)
        s = s + "+"
s = s[:-1]
print(s)
