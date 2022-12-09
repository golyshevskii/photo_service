from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewPostForm
from .models import Photo


@login_required(login_url='/auth/login/')
def main_page(request):
    """Function for rendering main page"""

    photo = Photo.objects.all()
    return render(request, 'base.html', context={'photo': photo})


@login_required(login_url='/auth/login/')
def new_post_page(request):
    """Function for creation of a new post"""

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yourposts')
    else:
        form = NewPostForm()
    
    return render(request, 'newpost.html', context={'form': form})


@login_required(login_url='/auth/login/')
def your_posts_page(request):
    """Function for render posts created by user"""

    photo = Photo.objects.filter(user=request.user.id).all()
    
    return render(request, 'yourposts.html', context={'photo': photo})


def signup_page(request):
    """Function for sign up process"""

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainpage')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', context={'form': form})