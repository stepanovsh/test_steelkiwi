from django.contrib import admin
from .models import Group
from student.models import Student

class Inline(admin.TabularInline):
    model = Student
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'chief']
    inlines = [Inline]

admin.site.register(Group, GroupAdmin)
