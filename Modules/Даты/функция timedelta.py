# основная статья: https://tirinox.ru/timedelta/
from datetime import datetime, timedelta

# прибавит к текущей дате выбранные параметры
print(str(datetime.now() + timedelta(days=133, hours=12, seconds=33, minutes=14)))
