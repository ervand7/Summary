from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

# Daylight saving time
dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
print(dt)  # 2020-10-31 12:00:00-07:00

# Standard time
dt += timedelta(days=7)
print(dt)  # 2020-11-07 12:00:00-08:00
print(dt.tzname())  # PST
