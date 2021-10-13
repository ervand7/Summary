# статья: https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html
from pandas import Timedelta

time_ = '7 days'
time_2 = '7 seconds'
time_3 = '7 minutes'
time_4 = '7 hours'
time_5 = '7 milliseconds'
time_6 = '7 microseconds'


print(Timedelta(time_))  # 7 days 00:00:00
print(Timedelta(time_2))  # 0 days 00:00:07
print(Timedelta(time_3))  # 0 days 00:07:00
print(Timedelta(time_4))  # 0 days 07:00:00
print(Timedelta(time_5))  # 0 days 00:00:00.007000
print(Timedelta(time_6))  # 0 days 00:00:00.000007

print(Timedelta("1 days 2 hours"))
print(Timedelta("P0DT0H1M0S"))
