from django.core.management.base import BaseCommand

class Command( BaseCommand ):
    option_list = BaseCommand.option_list

    requires_model_validation = True

    def handle(self, *args, **options):

        from group.models import Group

        lines = []

        q = Group.objects.all()
        for group in q:
            lines.append( "Group name: %s, Students: %d" % (group.name, group.students.count() ))

        return "\n".join( lines )