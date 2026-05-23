from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class productmodel(models.Model):
    pname = models.CharField(max_length=20)
    pdesc = models.CharField(max_length=30)
    price = models.IntegerField()
    pcategory =models.CharField(max_length=30)
    pqauntity = models.IntegerField()
    trending = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    pimage = models.ImageField(upload_to='uploads/', default='dfimg.jpg.jpeg')
    is_delete = models.BooleanField(default=False)
class cartmodel(models.Model):
    pname = models.CharField(max_length=20)
    price = models.IntegerField()
    pcategory =models.CharField(max_length=30)
    pqauntity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    host = models.ForeignKey(User,on_delete=models.CASCADE)