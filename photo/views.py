from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def main_page(request):
    """Function for render main page"""

    return render(request, 'base.html')
