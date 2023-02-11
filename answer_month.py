"""2. Написать программу, которая спрашивает у пользователя номер месяца и выводит,
к какому сезону относится данный месяц (осень, зима, весна, лето)"""
winter = "Зима"
spring = "Весна"
summer = "Лето"
autumn = "Осень"
a = input()
if a == '12':
    print(winter)
elif a == '1':
    print(winter)
elif a == '2':
    print(winter)
elif a == '3':
    print(spring)
elif a == '4':
    print(spring)
elif a == '5':
    print(spring)
elif a == '6':
    print(summer)
elif a == '7':
    print(summer)
elif a == '8':
    print(summer)
elif a == '9':
    print(autumn)
elif a == '10':
    print(autumn)
elif a == '11':
    print(autumn)
else:
    print("Такого месяца нет")
