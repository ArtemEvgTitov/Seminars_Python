# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Input number: '))
slovar = {}
i = 1
while i <= number:
    slovar[i] = 3 * i + 1
    i +=1

print(slovar)