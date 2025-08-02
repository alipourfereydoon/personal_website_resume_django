from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=20,verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey(User,on_delete= models.CASCADE,verbose_name='نویسنده')
    category = models.ManyToManyField(Category,related_name='articles', verbose_name='دسته بندی')
    title = models.CharField(max_length=70, verbose_name='عنوان')
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(null=True , unique=True)
    # class Meta:
    #     ordering = ('-created',)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self' , on_delete=models.CASCADE ,null=True , blank=True , related_name='repleies')

    class Meta:
        verbose_name = 'نظر '
        verbose_name_plural = 'نظرات '

    def __str__(self):
        return self.body[:30]

class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.TextField(max_length=200, verbose_name='متن')
    email = models.EmailField(verbose_name='ایمیل')
    age = models.IntegerField(default=0, verbose_name='سن')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.title
    