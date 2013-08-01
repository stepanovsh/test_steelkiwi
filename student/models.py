from django.db import models


class Student(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50 )
    surname = models.CharField(verbose_name="Surname", max_length=100)
    father = models.CharField(verbose_name="Father", max_length=100)
    birthday = models.DateField(verbose_name="Berthday")
    student_card =  models.CharField(verbose_name="Student Card",  max_length=50)
    group = models.ForeignKey('group.Group', verbose_name="Group", related_name='students')

    class Meta:
        ordering = ['surname', 'name']

    def __unicode__(self):
        return "%s %s %s" % (self.surname, self.name, self.father)
