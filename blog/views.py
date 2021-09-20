from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_on']


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def CategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat)
    return render(request, 'categories.html', {'cat': cat})
