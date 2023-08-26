from src.calendarmodule_7.utils import *
month, day, year = map(int, input().split(' '))
calendar_result = weekday(month, day, year)
print(calendar_result)
