# 2. Make a variable named month_short which takes a 3
# character short string of month.
# Then write the if/elif/else, such that the program print
# “January” for month_short = “Jan”, …, “December” for
# month_short = “Dec” and “Unknow” if month_short is
# anything we don’t have anticipated.

month_short = "APR"

if month_short == 'JAN':
    print("JANUARY")
elif month_short == 'FEB':
    print("FEBRUARY")
elif month_short == 'MAR':
    print("MARCH")
elif month_short == 'APR':
    print("APRIL")
elif month_short == 'MAY':
    print("MAY")
elif month_short == 'JUN':
    print("JUNE")
elif month_short == 'JUL':
    print("JULY")
elif month_short == 'AUG':
    print("AUGUST")
elif month_short == 'SEP':
    print("SEPTEMBER")
elif month_short == 'OCT':
    print("OCTOBER")
elif month_short == 'NOVEMBER':
    print("NOVEMBER")
elif month_short == 'DEC':
    print("DECEMBER")
else:
    print("Unknown")