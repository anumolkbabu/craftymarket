from django.db import models

# Create your models here.
class Roles(models.Model):
    rolename = models.CharField(max_length=25)
class Login(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='', null=True)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    password = models.CharField(max_length=200)
    roleid = models.ForeignKey(Roles, on_delete=models.CASCADE)