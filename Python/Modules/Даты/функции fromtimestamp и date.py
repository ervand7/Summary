from datetime import datetime

st_ctime = 1621146723
my_time = datetime.fromtimestamp(st_ctime)
print(my_time)  # 2021-05-16 09:32:03
print(my_time.date())  # 2021-05-16
