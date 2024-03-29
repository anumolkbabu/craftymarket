from django.db import models

# Create your models here.
class Roles(models.Model):
    roleid=models.AutoField(primary_key=True,verbose_name='roleid')
    rolename = models.CharField(max_length=25)
class Login(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone =models.CharField(max_length=12)
    password = models.CharField(max_length=200)
    craftmaker = models.BooleanField(default=False)
    # roleid = models.ForeignKey(Roles, on_delete=models.CASCADE)
class Category(models.Model):
    categoryid=models.AutoField(primary_key=True, verbose_name='categoryid')
    categoryname=models.CharField(max_length=100)
class Product(models.Model):
    pid=models.AutoField(primary_key=True,verbose_name='pid')
    pname=models.CharField(max_length=100)
    pprize=models.IntegerField()
    pdescription=models.CharField(max_length=100)
    prating=models.IntegerField()
    pthumbnail=models.CharField(max_length=100)
    pimage=models.ImageField(upload_to='productimages/')
    categoryid=models.ForeignKey(Category, on_delete=models.CASCADE)
class Order(models.Model):
    oid=models.AutoField(primary_key=True,verbose_name='oid')
    address=models.CharField(max_length=100)
    selectpayment=models.IntegerField()
    

