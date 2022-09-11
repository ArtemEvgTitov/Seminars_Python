# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов в виде списка 
# Для N = 5: 1, -3, 9, -27, 81

number = int(input('Введите число '))
list = []
for i in range(0, number-1):
    list.append((-3)**i)
else:
    list.append((-3)**(number-1))
print(list)