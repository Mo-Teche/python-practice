# ver= 'day 17 starts now'
# print(ver.title())

# import datetime
# time = datetime.datetime.now()
# time_now= time.strftime(' %m/%d/%Y:   %H:%M:%S ')
# print(time_now)

# data = input('Enter some number here : ')
# lists = data.split('#')
# tuples = tuple(lists)
# print(lists)
# print(tuples)

# filename = input('Enter file name : ').split('.')
# print(f' {filename} extension is {filename[-1]}')



# import calendar
# print(calendar.month(2022 ,11 ))
from datetime import date
fd = int(input(' First Days  :'))
fm = int(input(' First Month : '))
fy = int(input(' First Years : '))

import datetime
time = datetime.datetime.now()
time_now = int(time.strftime('%Y,%m,%d'))

f_date =date(fy, fm, fd)
boyos = (time_now - f_date)/365
print(boyos.days)
