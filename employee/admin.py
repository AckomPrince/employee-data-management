from django.contrib import admin
from .models import Employee, Log, Supervisor
# Register your models here.


admin.site.register(Employee)
admin.site.register(Supervisor)
admin.site.register(Log)