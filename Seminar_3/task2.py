# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# st = "qwe"
# task_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
# ind = 0
# sh = 0
# m_ind = 0
# for i in task_list:
#     if i == st and sh < 2:
#         sh += 1
#         m_ind = ind
#     ind += 1

# if sh != 0:
#     print(f"{task_list} - ищем: {st}, ответ {m_ind} индексе")
# else:
#     print('-1')

data = ["123", "234", 123, "567"]

def second(data, qwe):
    count = 0
    count2 = 0
    for i in data:

        if qwe == i:
            count2 += 1
        if count2 > 1:
            return count
        count += 1
    return -1
print(second(data, "123"))