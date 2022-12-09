from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Photo


class NewPostForm(forms.ModelForm):
    """Form for a new post creation"""
    
    class Meta:
        model = Photo
        fields = ('img', 'title', 'desc', 'people', 'location', 'tags',)
        exclude = ('user',)


class SignUpForm(UserCreationForm):
    """Form for a new user registration"""
    
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
