# пишем конвертор по этой документации:
# https://docs.djangoproject.com/en/3.2/topics/http/urls/
from datetime import datetime


class DateConverter:
    """Внимание! regex, to_python, to_url - это зарезервированные имена!"""
    regex = '[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'

    def to_python(self, value: str) -> datetime:
        """Принимаем строку и возвращаем время"""
        return datetime.strptime(value, '%Y-%d-%m')

    def to_url(self, value: datetime) -> str:
        """Принимаем время и возвращаем строку"""
        return value.strftime(value)
