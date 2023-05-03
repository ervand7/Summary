# функция strftime есть и в модуле datetime, и в модуле time
import datetime
import time

# strptime преобразует строку в формат datetime
# strptime преобразует datetime в формат строки
my_time = datetime.datetime.strptime('2020-12-12', '%Y-%d-%m')
print(my_time)  # 2020-12-12 00:00:00
my_str = datetime.datetime.strftime(my_time, '%Y-%d-%m')
print(my_str)  # 2020-12-12

print('__________________________')

print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))  # 02.03.2021 19:04:48
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 2021-03-02 19:04:48
print(time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime()))  # 2021-03-21_05-41-03
print(
    time.gmtime())  # time.struct_time(tm_year=2021, tm_mon=3, tm_mday=21, tm_hour=5, tm_min=41, tm_sec=3, tm_wday=6, tm_yday=80, tm_isdst=0)
