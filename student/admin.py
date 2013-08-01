from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('surname', 'group')



admin.site.register(Student, StudentAdmin)
