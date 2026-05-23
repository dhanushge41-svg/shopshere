from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    pimage = models.ImageField(upload_to='uploads/' ,default='dfimg.jpg.jpeg')
    host = models.ForeignKey(User,on_delete=models.CASCADE)