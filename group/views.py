# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView,  DeleteView
from .models import Group
from django.core.urlresolvers import reverse,reverse_lazy

class GroupView(ListView):
    model = Group
    template_name = "group/group.html"
    context_object_name = 'group_list'

class GroupAddView(CreateView):
    model = Group
    success_url = reverse_lazy("index")
    template_name = "group/add_group.html"

class GroupEditView(UpdateView):
    model = Group
    success_url = reverse_lazy("index")
    template_name = "group/add_group.html"

class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy("index")



