from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import main_page, signup_page


urlpatterns = [
    path('', main_page, name='mainpage'),
    path('auth/login/', LoginView.as_view(template_name="login.html"), name='loginpage'),
    path('auth/logout/', LogoutView.as_view(), name='logoutpage'),
    path('auth/signup/', signup_page, name='signuppage'),
]