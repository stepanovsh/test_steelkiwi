from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name="Group Name",  max_length=50)
    chief = models.ForeignKey('student.Student', blank=True, null=True,
                              on_delete=models.SET_NULL, verbose_name="Elder Student Group", related_name='chief')

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return "%s" % self.name

    #@models.permalink
    def get_absolute_url(self):
        return 'group_view/%i/' % self.pk
        #return ('group_view', [str(self.pk)])