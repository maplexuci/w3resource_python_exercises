# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.


import calendar


def cal(yyyy, mm):
    return calendar.month(yyyy, mm)


print(cal(2020, 6))  # Need to print the return value of the function.
