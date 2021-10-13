from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

rd = relativedelta(years=3, months=7, days=18)
print(rd)
# I use 'now', but you may want to adjust your start and end range to a specific set of dates.
now = datetime.now()
print(now)

# calculate the date difference from the relativedelta span
then = now - rd
print(then)  # unlike normal timedelta 'then' is returned as a datetime
# subtracting two dates will give you a timedelta which contains the value you're looking for
diff = now - then
print(diff)
