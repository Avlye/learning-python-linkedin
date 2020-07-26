from datetime import date, time, datetime

# Get today's date
today = date.today()
print('Today\'s date is', today)

# Print out the date's individual components
print('Date:', today.day, '/', today.month, '/', today.year)

days = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
]
print('Today\'s weekday number is', today.weekday())
print('Today is', days[today.weekday()])

# Time now!
print('Now:', datetime.now())