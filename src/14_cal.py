"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# get month and year from user
current_month = datetime.now().month
current_year = datetime.now().year
c = calendar.TextCalendar(calendar.SUNDAY)

# Each input given by the user gets appended to the list
x = input().split()

# if no inputs, print out a calendar for current date
if not x:
    print(c.formatmonth(current_year, current_month))
elif len(x) == 1:
    print(c.formatmonth(current_year, int(x[0])))
elif len(x) == 2:
    print(c.formatmonth(int(x[1]), int(x[0])))
else:
    print('Please enter a month followed by a year')


# if one input, assume month, print calendar for that month

# if two inputs, assume month year, print calendar for that month/year

# if more than two inputs, print usage
