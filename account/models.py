from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=20, verbose_name='نام پدر')
    nationalcode = models.CharField(max_length=12, verbose_name='کد ملی')
    image = models.ImageField(upload_to='profile', null=True , blank=True , verbose_name='تصویر')

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'

    def __str__(self):
        return self.user.username
    
    


    
    
class Login(models.Model):
    username = models.CharField(max_length=15,verbose_name='نام کاربری')
    password = models.CharField(max_length=12, verbose_name='پسورد') 

    class Meta:
        verbose_name = 'ورود به حساب کاربری'
        verbose_name_plural = 'ورود به حساب های کاربری'

    def __str__(self):
        return self.username   
