from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default='Default')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    intro = models.CharField(max_length=100)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '  |  ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
