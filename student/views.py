from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Student
from group.models import Group
from django.views.generic.edit import CreateView, UpdateView,  DeleteView, FormView
from django.core.urlresolvers import reverse, reverse_lazy
from .forms import StudentForm

class StudentsView(ListView):
    """
    Students View
    """
    model = Student
    template_name = 'student/student.html'
    context_object_name = "students_list"
    def get_queryset(self):
        return Student.objects.filter(group = self.args[0])


class StudentsAddView(CreateView):
    """
    Add Student
    """
    model = Student
    success_url = reverse_lazy('group')
    template_name = 'student/add_student.html'


class StudentsAddViewWithPk(FormView):
    form_class = StudentForm
    template_name = "student/add_student.html"
    success_url = reverse_lazy('group')
    

    def form_valid(self, form):
        form.save()
        return super(StudentsAddViewWithPk, self).form_valid(form)



class StudentsEditView(UpdateView):
    """
    Edit student
    """
    model = Student
    success_url = reverse_lazy('group')
    template_name = 'student/add_student.html'

class StudentsDeleteView(DeleteView):
    """
    Delete student
    """
    model = Student
    #success_url = reverse_lazy('group')
