from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Load app
from group.views import GroupView, GroupAddView, GroupEditView, GroupDeleteView
from student.views import StudentsView, StudentsAddView, StudentsEditView, StudentsDeleteView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    # Group view:
    url(r'^$', GroupView.as_view(), name='index'),
    url(r'^add_group/$', login_required(GroupAddView.as_view(), login_url=('/login/')), name='add_group'),
    url(r'^edit_group/(?P<pk>\d+)/$', login_required(GroupEditView.as_view(), login_url=('/login/')), name='edit_group'),
    url(r'^del_group/(?P<pk>\d+)/$', login_required(GroupDeleteView.as_view(), login_url=('/login/')), name='del_group'),

    #Students view
    url(r'^group_view/(\d+)/$', StudentsView.as_view(), name='student_list'),
    url(r'^add_student/$', login_required(StudentsAddView.as_view(), login_url=('/login/')), name='add_student'),
    url(r'^edit_student/(?P<pk>\d+)/$', login_required(StudentsEditView.as_view(), login_url=('/login/')), name='edit_student'),
    url(r'^del_student/(?P<pk>\d+)/$', login_required(StudentsDeleteView.as_view(), login_url=('/login/')), name='del_student'),


    # url(r'^test_steelkiwi/', include('test_steelkiwi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #Login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login/'}, name='logout'),
    url(r'^accounts/profile/', RedirectView.as_view(url = reverse_lazy('index')), {'url': '/'}),
)
