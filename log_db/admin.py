from django.contrib import admin
from .models import LogDB

class AdminLogDB(admin.ModelAdmin):
    list_display = ['create_time', 'model_name', 'action']

admin.site.register(LogDB, AdminLogDB)



