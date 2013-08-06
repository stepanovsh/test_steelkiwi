from django.core.urlresolvers import reverse,reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _u
from student.models import Student


class Group(models.Model):

    name = models.CharField(verbose_name=_u("Group Name"),  max_length=50, unique=True)
    chief = models.ForeignKey(Student, blank=True, null=True,
                              on_delete=models.SET_NULL, verbose_name=_u("Elder Student Group"), related_name='chief')


    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return "%s" % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('student_list', [self.pk])

    @models.permalink
    def get_edit_url(self):
        return ('edit_group' , [self.pk])

    @models.permalink
    def get_del_url(self):
        return ('del_group',  [self.pk])