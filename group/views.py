# Create your views here.
from django.views.generic import ListView
from .models import Group

class GroupView(ListView):
    model = Group
    template_name = "group.html"
    context_object_name = 'group_list'