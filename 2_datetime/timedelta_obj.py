from datetime import timedelta, datetime, date

print("One year from now will be", datetime.now() + timedelta(days=365))
print("3 weeks from now will be", datetime.now() + timedelta(weeks=3))

## How many days until April Fools
today = date.today()
april_fools_date = date(today.year, 4, 1)

if april_fools_date < today:
    april_fools_date = april_fools_date.replace(year=today.year + 1)

time_to_april_fools = april_fools_date - today

print("Days until april fools day: ", time_to_april_fools)