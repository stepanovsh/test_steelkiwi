from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Load app
from group.views import GroupView, GroupAddView, GroupEditView, GroupDeleteView
from student.views import StudentsView, StudentsAddView, StudentsEditView, StudentsDeleteView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', GroupView.as_view(), name='index'),
    url(r'^group_view/(\d+)/$', StudentsView.as_view(), name='student_list'),
    url(r'^add_group/$', GroupAddView.as_view(), name='add_group'),
    url(r'^Edit_group/(?P<pk>\d+)/$', GroupEditView.as_view(), name='edit_group'),
    url(r'^del_group/(?P<pk>\d+)/$', GroupDeleteView.as_view(), name='del_group'),

    url(r'^add_student/$', StudentsAddView.as_view(), name='add_student'),

    url(r'^edit_student/(?P<pk>\d+)/$', StudentsEditView.as_view(), name='edit_student'),
    url(r'^del_student/(?P<pk>\d+)/$', StudentsDeleteView.as_view(), name='del_student'),
    # url(r'^test_steelkiwi/', include('test_steelkiwi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
