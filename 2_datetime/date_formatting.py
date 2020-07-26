from datetime import datetime

now = datetime.now()
print(now.strftime('%Y - %A'))
print(now.strftime('%y - %a - %d %B %x %c'))
print(now.strftime('%H:%M:%s'))