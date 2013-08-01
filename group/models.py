from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name="Group Name",  max_length=50)
    chief = models.ForeignKey('student.Student', blank=True, null=True,
                              on_delete=models.SET_NULL, verbose_name="Elder Student Group", related_name='chief')

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return "%s" % self.name