from datetime import date
import calendar

today = date.today()
c = calendar.TextCalendar(calendar.SUNDAY)
this_month = c.formatmonth(today.year, today.month, 0, 0)
next_month = c.formatmonth(today.year, today.month + 1, 0, 0)

print()
print(this_month)
print(next_month)