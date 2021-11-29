from django.db import models

# Create your models here.
class SignUp(models.Model):
    Name=models.CharField(max_length=20, default='')
    Place=models.CharField(max_length=20,default='')
    Email=models.EmailField(default='')
    Password=models.CharField(max_length=8,default='')
    Photo=models.ImageField(upload_to='media',null=True,blank=True,default='')
