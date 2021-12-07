from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

rd = relativedelta(years=3, months=7, days=18)
print(rd)  # relativedelta(years=+3, months=+7, days=+18)
# I use 'now', but you may want to adjust your start and end range to a specific set of dates.
now = datetime.now()
print(now)  # 2021-12-07 23:39:22.340299

# calculate the date difference from the relativedelta span
then = now - rd

# unlike normal timedelta 'then' is returned as a datetime
print(then)  # 2018-04-19 23:39:22.340299

# subtracting two dates will give you a timedelta which contains the value you're looking for
diff = now - then
print(diff)  # 1328 days, 0:00:00
