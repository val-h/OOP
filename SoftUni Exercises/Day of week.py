from datetime import datetime as dt
day = input('Date: ')
targetDate = [int(x) for x in day.split('-')]
date = dt(targetDate[2], targetDate[1], targetDate[0])

if date.weekday() == 0: print('Monday')
elif date.weekday() == 1: print('Tuesday')
elif date.weekday() == 2: print('Wednesday')
elif date.weekday() == 3: print('Thursday')
elif date.weekday() == 4: print('Friday')
elif date.weekday() == 5: print('Saturday')
elif date.weekday() == 6: print('Sunday')
