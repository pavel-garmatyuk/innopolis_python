# Найдите сумму и произведение элементов списка. Результаты вывести в консоль.
arr = [3, 5, 12, 17, 21]
sum_arr = 0
mult_arr = 1

for i in arr:
    sum_arr += i
    mult_arr *= i

print("Исходный список", *arr)
print("Сумма элементов списка", sum_arr)
print("Произведение элементов списка", mult_arr)