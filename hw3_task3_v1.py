"""
Есть список a = [1, 2, 3, 4, 5, 6].
Требуется удалить из этого списка все нечетные значения, а четные разделить на 2.
Всю операции производить с текущим списком, второй список создавать нельзя. Вывести измененный список в консоль.
"""
a = [1, 2, 3, 4, 5, 6]
for i in range(len(a) - 1, -1, -1):
    if a[i] % 2 != 0:
        a.pop(i)
    elif a[i] % 2 == 0:
        a[i] = a[i] // 2

print(*a)
