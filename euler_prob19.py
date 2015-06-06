
# SUBPROBLEMS:
# - start on 1,1,1900 (1, Jan mo 1, 1900 yr) = Monday
# - determine if leap year
#     - if %4 == 0, but not %100 == 0 (unless also %400 == 0)
# - 365 evenly divides by 7.  365/7 = 52.

# - starts 1, 1, 1901
# - determine if 1900 was leap year
#     - if no, then 1, 1, 1901 = Monday
#     - if yes, then 1, 1, 1901 = Tuesday

# - starting 1901 to 2001
#     - for each year
#             - start_day_of_week = 1...7
#             - if not leap year = sundays + 52
#             - if leap year,
#                 if start_day_of_week = 7,
#                     sundays + 53
#             - update for next year,
#                 if leap year
#                     start_day_of_week += 1
#                 if start_day_of_week > 7
#                     start_day_of_week = 1

# 1900/400 = 4.  is a leap year.
# 1901 start_day_of_week = Tuesday


def count_sundays(start_yr, end_yr, start_day_of_week):
    count = 0

    for yr in range(start_yr, end_yr+1):

        array_dates = array_days_of_week(is_leap_yr(yr))

        # determine dates idx which = a sunday
        idx_sundays = 7 - start_day_of_week

        while idx_sundays < len(array_dates):
            date = array_dates[idx_sundays]
            if date == 1:
                count += 1
            idx_sundays += 7

        if is_leap_yr(yr):
            start_day_of_week += 1

        if start_day_of_week > 7:
            start_day_of_week = 1

    return count


def array_days_of_week(is_leap_yr):
    not_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap = [31,29,31,30,31,30,31,31,30,31,30,31]

    if is_leap_yr:
        days_in_mo = leap
    else:
        days_in_mo = not_leap

    days_in_yr = []

    for x in range(len(days_in_mo)):
        for d in range(1, days_in_mo[x]+1):
            days_in_yr.append(d)

    return days_in_yr


def is_leap_yr(yr):
    if yr % 4 != 0:
        return False
    elif yr % 400 == 0:
        return True
    else:
        return True


# 1901 start_day_of_week = Tuesday
# 7 = Sunday
# 1 = Monday
# 2 = Tuesday

print count_sundays(1901, 2000, 2)
