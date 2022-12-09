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
        form = NewPostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('yourpostspage')
    else:
        form = NewPostForm()
    
    return render(request, 'newpost.html', context={'form': form})


@login_required(login_url='/auth/login/')
def your_posts_page(request):
    """Function for render posts created by user"""

    photo = Photo.objects.filter(user=request.user.id).all()
    
    return render(request, 'yourposts.html', context={'photo': photo})


@login_required(login_url='/auth/login/')
def search_page(request):
    """Function for render posts by search bar"""
    
    if request.method == 'POST':
        search = request.POST['search_tags']
        photo = Photo.objects.filter(tags__contains=search).all()
    else:
        search = None
        photo = None
    
    return render(request, 'search.html', context={'photo': photo, 'search': search})


@login_required(login_url='/auth/login/')
def filter_page(request):
    """Function for render posts by filter"""
    
    if request.method == 'POST':
        filter_title = request.POST['title']
        filter_date = request.POST['date']
        filter_people = request.POST['people']
        filter_location = request.POST['location']
        photo = Photo.objects.filter(title__contains=filter_title,
                                     cr_dt__contains=filter_date,
                                     people__contains=filter_people,
                                     location__contains=filter_location).all()
    else:
        filter_title, filter_date, filter_people, filter_location = None, None, None, None
        photo = None
    
    return render(request, 'filter.html', context={'photo': photo,
                                                   'filter_title': filter_title,
                                                   'filter_date': filter_date,
                                                   'filter_people': filter_people,
                                                   'filter_location': filter_location})

@login_required(login_url='/auth/login/')
def photo_details_page(request, id):
    photo = Photo.objects.filter(id=id).first()
    return render(request, 'photodetails.html', context={'photo': photo})


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