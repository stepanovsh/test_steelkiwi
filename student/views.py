from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Student
from group.models import Group

class StudentsView(ListView):
    model = Student
    template_name = 'student.html'
    context_object_name = "students_list"
    def get_queryset(self):
        return Student.objects.filter(group = self.args[0])