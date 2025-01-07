"""
Write a function that takes a year as a
parameter and returns true if the year
is a leap year, otherwise false.
3 criteria must be taken into consideration:
1 - the year is evenly divisible by 4
2 - if the year can be evenly divided
by 100, it is not a leap year unless
3 - the year is also evenly divisible
by 400
"""

def is_leap_year(year):
    return (year % 4 == 0 and (year % 100 ==0 or year % 400 == 0))
