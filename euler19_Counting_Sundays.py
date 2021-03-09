# Counting Sundays
from time import time


def e19():
    ystart = int(input("Enter the start year 1900 or more: "))
    mstart = int(input("Enter the start month 1-12: "))
    yend = int(input("Enter the last year equals start or more: "))
    mend = int(input("Enter the last month 1-12: "))
    start = time()
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    for y in range(1900, ystart + 1):
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            months[1] = 29
        else:
            months[1] = 28
        days += sum(months)
    days -= sum(months[mstart - 1:])
    wd = (days + 1) % 7  # determining the start week day of the interval
    print("The start week day is", wd)  # 0 is Sunday, 1 is Monday, etc.
    sundays = 0
    for y in range(ystart, yend + 1):
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            months[1] = 29
        else:
            months[1] = 28
        if y == ystart:
            for m in months[mstart - 1:]:
                if wd == 0:
                    sundays += 1
                wd = (wd + m) % 7
        elif y == yend:
            for m in months[:mend]:
                if wd == 0:
                    sundays += 1
                wd = (wd + m) % 7
        else:
            for m in months:
                if wd == 0:
                    sundays += 1
                wd = (wd + m) % 7

    print(f"There are {sundays} sundays fell on the 1st of the month during your period of time")
    print('Runtime =', time() - start)


e19()  # 171 (from 01/1901 to 12/2000)
