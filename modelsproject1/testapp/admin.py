from django.contrib import admin
from testapp.models import Employee
from testapp.models import Custmor

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eadd']
class CustmorAdmin(admin.ModelAdmin):
    list_display=['custname','custemail','custadhornumber','custphonenumber','custage']


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Custmor,CustmorAdmin)
