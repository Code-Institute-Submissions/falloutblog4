from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class Home(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
