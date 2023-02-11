from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    # студенты, к которым еще не добавлены учителя
    students_before = Student.objects.all()
    teachers = Teacher.objects.all()

    # добавляем учителей к студентам
    for student in students_before:
        for teacher in teachers:
            student.teacher.add(teacher)  # student.teacher - это поле m2m из Student

    students_after = Student.objects.order_by('-group').all().prefetch_related('teacher')
    context = {'students': students_after}

    return render(
        request=request, template_name='school/students_list.html', context=context
    )

