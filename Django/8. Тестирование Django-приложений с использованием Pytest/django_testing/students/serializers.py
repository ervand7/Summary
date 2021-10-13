from rest_framework import serializers
from django.conf import settings
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, attrs):
        """
        Проверка на максимальное кол-во студентов на курсе.
        """
        if 'students' in attrs:
            if len(attrs['students']) > settings.MAX_STUDENTS_PER_COURSE:
                raise serializers.ValidationError(
                    'На одном курсе может быть не более 20 студентов!'
                )

        return attrs
