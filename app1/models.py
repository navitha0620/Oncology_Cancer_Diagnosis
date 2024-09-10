from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Register(models.Model):
    email=models.EmailField(primary_key=True,max_length=50,unique=True)
    password=models.CharField(max_length=50,unique=True)
    contact=models.CharField(max_length=10,unique=True)
    hospitalname=models.CharField(max_length=100)
   # UMR=models.CharField(max_length=7)
    branchaddress=models.CharField(max_length=50)
   # firstname=models.CharField(max_length=100)
    subject=models.CharField(max_length=150)
    design=models.CharField(max_length=15,default="user")
    #department=models.CharField(max_length=50)
    #doctor=models.CharField(max_length=100)


    def __str__(self):
        #return self.email+","+self.
        return self.email
"""
def clean(self):
    if Register.objects.filter(email=self.email).exists():
       raise ValidationError({'email': 'This email is already registered.'})
    if Register.objects.filter(password=self.password).exists():
        raise ValidationError({'password': 'This password is already in use.'})
    if Register.objects.filter(contact=self.contact).exists():
        raise ValidationError({'contact': 'This contact number is already registered.'})
"""
    