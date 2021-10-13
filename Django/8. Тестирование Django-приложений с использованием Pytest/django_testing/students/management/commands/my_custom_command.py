from django.core.management.base import BaseCommand
from students.models import Course, Student
from mimesis import Person
from mimesis.enums import Gender
from django.conf import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        students_list = []
        for _ in range(settings.MAX_STUDENTS_PER_COURSE + 10):
            student_info = dict()
            student_info['name'] = Person('el').surname(gender=Gender.FEMALE)
            students_list.append(student_info)
        for item in students_list:
            student = Student(**{key: value for key, value in item.items() if key})
            student.save()

        Course.objects.create(
            name=Person('zh').surname(gender=Gender.FEMALE)
        )
