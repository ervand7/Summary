# хорошая официальная документация: https://dateparser.readthedocs.io/en/latest/
import dateparser
from datetime import datetime


a = dateparser.parse('6 minutes').replace(microsecond=0)
print(a)  # 2021-03-30 21:32:07
print(type(a))  # <class 'datetime.datetime'>

b = datetime.now().replace(microsecond=0) - dateparser.parse('6 minutes').replace(microsecond=0)
print(b)  # 0:06:00
print(type(b))  # <class 'datetime.timedelta'>

c = datetime.now() - dateparser.parse('5 hours')
print(c)  # 4:59:59.998319
print(type(c))  # <class 'datetime.timedelta'>

d = datetime.now().replace(microsecond=0) - dateparser.parse('2 days').replace(microsecond=0)
print(d)  # 2 days, 0:00:00
print(type(d))  # <class 'datetime.timedelta'>

e = datetime.now().replace(microsecond=0) - dateparser.parse('3 weeks').replace(microsecond=0)
print(e)  # 21 days, 0:00:00
print(type(e))  # <class 'datetime.timedelta'>

print('________________')

z = datetime.now().replace(microsecond=0)
z1 = dateparser.parse('3 weeks').replace(microsecond=0)
print(z)
print(z1)

s = dateparser.parse('March')
print(s)
print(type(s))

from dateparser.search import search_dates
print(search_dates('The first artificial Earth satellite was launched on 4 October 1957.'))