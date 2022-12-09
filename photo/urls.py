from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import main_page, signup_page, new_post_page, your_posts_page, search_page, filter_page, photo_details_page


urlpatterns = [
    path('', main_page, name='mainpage'),
    path('search/', search_page, name='searchpage'),
    path('filter/', filter_page, name='filterpage'),
    path('post/', new_post_page, name='newpostpage'),
    path('photodetails/<str:id>', photo_details_page, name='photodetailspage'),
    path('yourposts/', your_posts_page, name='yourpostspage'),
    path('auth/login/', LoginView.as_view(template_name="login.html"), name='loginpage'),
    path('auth/logout/', LogoutView.as_view(), name='logoutpage'),
    path('auth/signup/', signup_page, name='signuppage'),
]