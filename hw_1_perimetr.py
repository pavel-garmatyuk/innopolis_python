"""
Написать программу, которая спрашивает у пользователя длину сторон прямоугольника
и выводит площадь и периметр."""
print("Ведите длину сторон прямоугольника")
print("Сторона a: ")
a = int(input())
print("Сторона b: ")
b = int(input())
print("Площадь прямоугольника равна: ", a * b, " кв.см")
print("Периметр прямоугольника равен: ", 2*(a + b), " см")
