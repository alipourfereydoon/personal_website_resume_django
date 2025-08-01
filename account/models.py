from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=20)
    nationalcode = models.CharField(max_length=12)
    image = models.ImageField(upload_to='profile', null=True , blank=True)

    def __str__(self):
        return self.user.username
    


    
    
class Login(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=12) 

    def __str__(self):
        return self.username   
