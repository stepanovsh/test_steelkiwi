from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

#Load app
from group.views import GroupView, GroupAddView, GroupEditView, GroupDeleteView
from student.views import StudentsView, StudentsAddView, StudentsEditView, StudentsDeleteView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',

    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'index.html'}, name='index'),
    #url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
    # Group view:
    url(r'^group/$', GroupView.as_view(), name='group'),
    url(r'^group/add_group/$', login_required(GroupAddView.as_view(), login_url=('/login/')), name='add_group'),
    url(r'^group/edit_group/(?P<pk>\d+)/$', login_required(GroupEditView.as_view(), login_url=('/login/')), name='edit_group'),
    url(r'^group/del_group/(?P<pk>\d+)/$', login_required(GroupDeleteView.as_view(), login_url=('/login/')), name='del_group'),

    #Students view
    url(r'^student/group_view/(\d+)/$', StudentsView.as_view(), name='student_list'),
    url(r'^student/add_student/$', login_required(StudentsAddView.as_view(), login_url=('/login/')), name='add_student'),
    url(r'^student/edit_student/(?P<pk>\d+)/$', login_required(StudentsEditView.as_view(), login_url=('/login/')), name='edit_student'),
    url(r'^student/del_student/(?P<pk>\d+)/$', login_required(StudentsDeleteView.as_view(), login_url=('/login/')), name='del_student'),



    url(r'^admin/', include(admin.site.urls)),
    #Login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login/'}, name='logout'),
    url(r'^accounts/profile/', RedirectView.as_view(url = reverse_lazy('group')), {'url': '/group/'}),
)
