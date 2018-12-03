from django.shortcuts import render
from testapp.models import Employee
from testapp.models import Custmor
# Create your views here.
def  employee_page_views(request):
    employees=Employee.objects.all()
    return render(request,'testapp/home.html',{'employees':employees})
def custmor_info_views(request):
    custmors=Custmor.objects.all()
    return render(request,'testapp/cust.html',{'custmors':custmors})
