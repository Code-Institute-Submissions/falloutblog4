from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUp, EditProfileForm, PasswordChangingForm, ProfilePageForm
from blog.models import UserProfile


class CreateProfilePage(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = "registration/create_profile.html"


class EditProfilePage(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
    success_url = reverse_lazy('home')


class ShowProfilePage(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class UserRegister(generic.CreateView):
    form_class = SignUp
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordChange(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html')