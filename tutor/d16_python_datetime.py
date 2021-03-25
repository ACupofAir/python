from datetime import datetime
from datetime import date
from datetime import time

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Time formating
t = now.strftime('%H:%M:%S')
print('time:', t)
time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
print('time_one:', time_one)
time_two = now.strftime('%d/%m/%Y, %H:%M:%S')
print('time_two:', time_two)

# Using Date from datetime
d = date(2020, 1, 1)
print(d)
today = date.today()
print("Current year:", today.year)

# Time Objects to Represent Time
a = time()
print("a = ", a)

b = time(10, 30, 50)
print("b = ", b)
