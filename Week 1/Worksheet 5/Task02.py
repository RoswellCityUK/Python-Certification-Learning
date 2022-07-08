"""
Program validates month provided by User in format i.e. Jan, Feb, Mar
and give back number of days in that month for the given year.
"""


def check_month(month, year):
    month_dict = {"Jan": 31, "Feb": 28, "Mar": 31,
                  "Apr": 30, "May": 31, "Jun": 30,
                  "Jul": 31, "Aug": 31, "Sep": 30,
                  "Nov": 31, "Oct": 30, "Dec": 31}

    if month in month_dict.keys():
        if is_leap_year(year) and month_dict[month] == 28:
            return 29
    else:
        raise Exception("Bad month argument, try format i.e. Jan, Feb, Mar")

    return month_dict[month]


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


print(check_month("Feb", 1600))
