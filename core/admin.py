from django.contrib import admin
from .models import *
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('DepartmentId','DepartmentName')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('EmployeeId','EmployeeName','Department','DateOfJoining','ProfileName')

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)