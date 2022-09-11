# Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами [4, 5, 1, 6, 2, 8]

A = [4, 5, 1, 6, 2, 8]
sum = 0
poz_min = 0
poz_max = 0
i = 1
size = len(A)
while i < size:
    if A[i] > A[poz_max]:
        poz_max = i
    elif A[i] < A[poz_min]:
        poz_min = i
    i += 1
if poz_max > poz_min:
    for i in range(poz_min, poz_max+1):
        sum += A[i]
elif poz_max < poz_min:
    for i in range(poz_max, poz_min+1):
        sum += A[i]
else:
    sum = A[poz_max]
print(A, sum)
