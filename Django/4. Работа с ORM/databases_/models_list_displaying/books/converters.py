from datetime import date, datetime
from django.conf import settings


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = settings.FILES_DATE_PATTERN

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, self.format).date()

    def to_url(self, value: date) -> str:
        return value.strftime(self.format)
