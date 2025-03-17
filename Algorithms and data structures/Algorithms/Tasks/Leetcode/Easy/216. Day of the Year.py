# my solution
def day_of_year(date: str) -> int:
    leap_years = {i for i in range(2020, 1900, -4)}
    year = int(date[:4])
    month = int(date[5:7]) if date[5] != "0" else int(date[6])
    day = int(date[8:]) if date[8] != "0" else int(date[9])

    h = {
        1: 31,
        2: 28 if year not in leap_years else 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    result = 0
    for k, v in h.items():
        if k == month:
            result += day
            return result
        result += v


# ChatGPT solution
def day_of_year(date: str) -> int:
    # Extract year, month, and day from the input string
    year, month, day = map(int, date.split('-'))

    # Days in each month (for non-leap years)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year (only needed for February)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29  # Adjust February for leap years

    # Sum up the days of the previous months and add the current day's number
    return sum(days_in_month[:month - 1]) + day