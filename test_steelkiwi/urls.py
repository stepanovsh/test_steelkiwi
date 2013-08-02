from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Load app
from group.views import GroupView
from student.views import StudentsView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', GroupView.as_view(), name='index'),
    url(r'^group_view/(\d+)/$', StudentsView.as_view(), name='student_list'),
    # url(r'^test_steelkiwi/', include('test_steelkiwi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
