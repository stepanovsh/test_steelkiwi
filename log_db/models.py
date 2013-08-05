from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from group.models import Group
from student.models import Student

class LogDB(models.Model):
    create_time = models.DateTimeField(verbose_name='Create Time', auto_now=True)
    model_name = models.CharField(verbose_name='Model', max_length=30)
    action = models.CharField(verbose_name='Action', max_length=30)


    def __unicode__(self):
        return "%s: %s" % (self.create_time.strftime("%d.%m.%Y %H:%M"), self.action)

@receiver(pre_save, sender = Group)
@receiver(pre_save, sender = Student)
def save_model(sender,  instance, signal, *args, **kwargs):
    log = LogDB()
    log.model_name = str(sender)

    try:
        sender.objects.get(pk=instance.pk)
        log.action = 'Object Change'
    except sender.DoesNotExist:
        log.action = 'Object Create'
    log.save()


@receiver(post_delete, sender = Group)
@receiver(post_delete, sender = Student)
def delete_model(sender,  instance, signal, *args, **kwargs):
    log = LogDB()
    log.model_name = str(sender)
    log.action = 'Object Delete'
    log.save()




