# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3


task_list = ['gfh5', 'gfh2', '67', 'jy32', '3put']


def task_list_2(list):
    result = ''
    for i in list:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            result += i

    return result


number = input('Input number: ')
ind = 0
for i in task_list:
    t_el = task_list_2(i)
    if number == t_el:
        print(f"{task_list} - ищем {number} - найдено на {ind} индексе")
    ind += 1
