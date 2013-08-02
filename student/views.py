from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Student
from group.models import Group
from django.views.generic.edit import CreateView, UpdateView,  DeleteView
from django.core.urlresolvers import reverse,reverse_lazy

class StudentsView(ListView):
    model = Student
    template_name = 'student/student.html'
    context_object_name = "students_list"
    def get_queryset(self):
        return Student.objects.filter(group = self.args[0])

class StudentsAddView(CreateView):
    model = Student
    success_url = reverse_lazy('index')
    template_name = 'student/add_student.html'

class StudentsEditView(UpdateView):
    model = Student
    success_url = reverse_lazy('index')
    template_name = 'student/add_student.html'

class StudentsDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy("index")
