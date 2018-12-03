from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=65)
    esal=models.IntegerField()
    eadd=models.CharField(max_length=65)
class Custmor(models.Model):
    custname=models.CharField(max_length=65)
    custadhornumber=models.IntegerField()
    custemail=models.CharField(max_length=20)
    custphonenumber=models.IntegerField()
    custage=models.IntegerField()
