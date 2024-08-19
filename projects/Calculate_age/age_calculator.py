# age_calculator.py

import time
from calendar import isleap

def judge_leap_year(year):
    """Judge if a given year is a leap year."""
    return isleap(year)

def month_days(month, leap_year):
    """Return the number of days in a given month."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year else 28
    return 0

def calculate_age(name, age):
    """Calculate age in years, months, and days from the given age in years."""
    localtime = time.localtime(time.time())

    year = int(age)
    month = year * 12 + localtime.tm_mon
    day = 0

    begin_year = localtime.tm_year - year
    end_year = localtime.tm_year

    # Calculate days for full years
    for y in range(begin_year, end_year):
        day += 366 if judge_leap_year(y) else 365

    # Add days for months in the current year
    leap_year = judge_leap_year(localtime.tm_year)
    for m in range(1, localtime.tm_mon):
        day += month_days(m, leap_year)

    # Add days for current month
    day += localtime.tm_mday

    return {
        "name": name,
        "years": year,
        "months": month,
        "days": day
    }
