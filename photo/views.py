from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


@login_required(login_url='/auth/login/')
def main_page(request):
    """Function for render main page"""

    return render(request, 'base.html')


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