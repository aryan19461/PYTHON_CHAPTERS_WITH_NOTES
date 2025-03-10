import calendar


year = int(input("Enter year = "))
month = int(input("Enter month in Number = "))

calendar = calendar.month(year, month)

print(calendar)