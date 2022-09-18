# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

a = str(input("Введите числа через пробел: "))
list_of_str = a.split(" ")
list_of_num = []
print(list_of_str)
for i in list_of_str:
    list_of_num.append(int(i))
print(f'Наибольшее число равно {min(list_of_num)}, а наибольшее {max(list_of_num)}')

# второе решение
my_str=(1,3,4,5,6)
print(*my_str, sep=" ")

max_value=max(my_str, key=lambda i: int(i))
min_value=min(my_str, key=lambda i: int(i))

print(max_value)
print(min_value)