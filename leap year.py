#leap year
year = int(input('enter a year:'))
if (year % 4 == 0) or (year % 400 == 0):
    print('It is a leap year')
else:
    print('It is not a leap year')
