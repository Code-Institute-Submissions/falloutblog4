from django.urls import path
from .views import Home, ArticleDetail

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article-detail"),
]
