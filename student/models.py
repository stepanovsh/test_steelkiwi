from django.db import models


class Student(models.Model):
    surname = models.CharField(verbose_name="Surname", max_length=100)
    name = models.CharField(verbose_name="Name", max_length=50 )
    father = models.CharField(verbose_name="Father", max_length=100)
    birthday = models.DateField(verbose_name="Birthday")
    student_card =  models.CharField(verbose_name="Student Card",  max_length=50)
    group = models.ForeignKey('group.Group', verbose_name="Group", related_name='students')

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

