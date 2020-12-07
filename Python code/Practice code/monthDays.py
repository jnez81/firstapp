import calendar

def monthDays(year, month):
    year = 1996
    month = 2
    days = calendar.monthrange(year, month)
    return days

print(monthDays(0, 0))