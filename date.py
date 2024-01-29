from math import *


date = int(input('date: '))
month = input('month: ')
year = input('year: ')
res = int(year[2:]) // 4
res += date
month_key = {
    'January': 1,
    'February': 4,
    'March': 4,
    'April': 0,
    'May': 2,
    'June': 5,
    'July': 0,
    'August': 3,
    'September': 6,
    'October': 1,
    'November': 4,
    'December': 6
}
res += month_key[month]
if int(year) < 2000:
    res += (floor((2000 - int(year))//100)+1)
    for i in range(1900, int(year), -100):
        if i <= 1900:
            res += 1
if int(year) % 4 == 0 and month == 'January' or month == 'February':
    res -= 1
res += int(year[2:])
res %= 7
if res == 2:
    print(year, ' ', month, ' ', date, ' ', 'is ', 'Sunday')
elif res == 3:
    print(year, ' ', month, ' ', date, ' ', 'is ', 'Monday')
elif res == 4:
    print(year, ' ', month, ' ', date, ' ', 'is ', 'Tuesday')
elif res == 5:
    print(year, ' ', month, ' ', date, ' ', 'is ', 'Wednesday')
elif res == 6:
    print(year, ' ', month, ' ', date, ' ', 'is ', 'Thursday')
elif res == 0:
    print(year, ' ', month, ' ', date, ' ', 'is ', 'Friday')
else:
    print(year, ' ', month, ' ', date, ' ', 'is ', 'Saturday')
