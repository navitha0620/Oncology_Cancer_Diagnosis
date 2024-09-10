from django.db import models
from app1.models import Register
# Create your models here.


class Register(models.Model):
    email=models.EmailField(primary_key=True,max_length=50)
    #password=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    hospitalname=models.CharField(max_length=100)
    #branchaddress=models.CharField(max_length=50)
   # firstname=models.CharField(max_length=100)
    subject=models.CharField(max_length=150)
    Name=models.CharField(max_length=100)
    UMR=models.CharField(max_length=7)
    #design=models.CharField(max_length=15,default="UMR")
    #department=models.CharField(max_length=50)
    #doctor=models.CharField(max_length=100)
   # def __str__(self):
  #  related_register =models.OneToOneField(Register, on_delete=models.CASCADE)
  #  def __str__(self):
   #     return f"{self.Name} ({self.email})"S