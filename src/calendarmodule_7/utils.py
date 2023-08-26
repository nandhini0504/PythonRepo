import calendar
def weekday(month,day,year):
    mm, dd, yy = month, day, year
    print(calendar.day_name[calendar.weekday(yy, mm, dd)].upper())
    return calendar.day_name[calendar.weekday(yy, mm, dd)].upper()