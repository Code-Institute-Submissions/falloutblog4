from django.urls import path
from .views import UserRegister, UserEdit, PasswordChange, ShowProfilePage, EditProfilePage, CreateProfilePage
from django.contrib.auth import views as auth_views
from. import views

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit_profile'),
    path('password/', PasswordChange.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePage.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_page/profile/', EditProfilePage.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePage.as_view(), name='create_profile_page')
 ]
