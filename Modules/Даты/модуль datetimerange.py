from datetimerange import DateTimeRange

time_range = DateTimeRange("2015-03-22T10:00:00+0900", "2015-03-22T10:10:00+0900")
print("2015-03-22T10:05:00+0900" in time_range)  # True
print("2015-03-22T10:11:00+0900" in time_range)  # False
