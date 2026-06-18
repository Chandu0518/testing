from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=255,null=False)
    firstname=models.CharField(max_length=255,null=False)
    lastname=models.CharField(max_length=255,null=False)
    email=models.CharField(max_length=255,null=False,unique=True)
    password=models.CharField(max_length=255,null=False)
    location=models.CharField(max_length=255,null=False)
    mobile=models.CharField(max_length=255,null=False,unique=True)
    