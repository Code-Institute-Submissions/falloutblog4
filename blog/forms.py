from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'intro', 'author', 'category', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Here'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Content Here'}),
            'intro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is the post about?'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'intro', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Here'}),
            'intro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is the post about?'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Content Here'}),
            
        }
