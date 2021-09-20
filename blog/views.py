from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class Home(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'
