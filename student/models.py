from django.db import models
from django.utils.translation import ugettext_lazy as _u

class Student(models.Model):
    surname = models.CharField(verbose_name=_u("Surname"), max_length=100)
    name = models.CharField(verbose_name=_u("Name"), max_length=50 )
    father = models.CharField(verbose_name=_u("Father"), max_length=100)
    birthday = models.DateField(verbose_name=_u("Birthday"))
    student_card =  models.CharField(verbose_name=_u("Student Card"),  max_length=50,  unique=True)
    group = models.ForeignKey('group.Group', verbose_name=_u("Group"), related_name='students')

    class Meta:
        ordering = ['surname', 'name']


    def get_full_name(self):
        return "%s %s %s" % (self.surname, self.name, self.father)

    def __unicode__(self):
        return self.get_full_name()

    @models.permalink
    def get_edit_url(self):
        return ('edit_student' , [self.pk])

    @models.permalink
    def get_del_url(self):
        return ('del_student',  [self.pk])

