#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: April 12 2022
# Find the day of the week as well as if it is a leap year


def main():
    daystr = input("What day of the month is it: ")
    monthstr = input("Enter the number value of the month: ")
    yearstr = input("What year is it: ")
    try:
        day = int(daystr)
        month = int(monthstr)
        year = int(yearstr)
    except:
        print("You have to input integers greater that 0")
        main()
    if day < 0 or month < 0 or year < 0:
        print("You have to input integers greater than 0")
        main()
    doomsday = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    day_week = (
        year + (year // 4) - (year // 100) + (year // 400) + doomsday[month - 1] + day
    ) % 7
    if year % 4 == 0:
        if (year % 100 == 0) and (year % 400 != 0):
            print("This year is not a leap year")
        else:
            print("This year is a leap year")
    else:
        print("This year is not a leap year")
    match day_week:
        case 1:
            print("The day of the week is Monday")
        case 2:
            print("The day of the week is Tuesday")
        case 3:
            print("The day of the week is Wednesday")
        case 4:
            print("The day of the week is Thursday")
        case 5:
            print("The day of the week is Friday")
        case 6:
            print("The day of the week is Saturday")
        case 7:
            print("The day of the week is Sunday")


if __name__ == "__main__":
    main()
