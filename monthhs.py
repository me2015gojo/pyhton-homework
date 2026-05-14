import calendar

year = int(input("Enter year: "))

for month in range(1, 13):
    print(calendar.month(year, month))