from django.urls import path
from .views import Home, ArticleDetail, AddPost, UpdatePost, DeletePost

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article-detail"),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name="update-post"),
    path('article/<int:pk>/delete', DeletePost.as_view(), name="delete_post"),

]
