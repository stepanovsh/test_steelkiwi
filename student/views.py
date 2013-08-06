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
    template_name = 'student/add_student.html'


class StudentsAddViewWithPk(FormView):
    form_class = StudentForm
    template_name = "student/add_student.html"


    def get_success_url(self):
        return reverse('student_list',args=[int(self.kwargs['pk'])])

    def get_initial(self):
        self.initial = {}
        self.pk = Group.objects.get(pk = int(self.kwargs['pk']))
        self.initial.update(dict(group = self.pk))
        return self.initial


    def form_valid(self, form):
        form.save()
        return super(StudentsAddViewWithPk, self).form_valid(form)



class StudentsEditView(UpdateView):
    """
    Edit student
    """
    model = Student
    template_name = 'student/add_student.html'

class StudentsDeleteView(DeleteView):
    """
    Delete student
    """
    model = Student
    success_url = reverse_lazy('group')
