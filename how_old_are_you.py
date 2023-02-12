import datetime
print("В каком году ты родился?")
birth_year = int(input())
year_now = datetime.datetime.today().year
print("Тебе ", year_now - birth_year, " лет")