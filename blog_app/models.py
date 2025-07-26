from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(null=True , unique=True)
    # class Meta:
    #     ordering = ('-created',)


    def __str__(self):
        return self.title