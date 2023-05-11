from django.urls import path, re_path
import re
from .views import register_view, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', register_view, name='Registration'),
    path('login/', login_view, name='Login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='Login'), name='Logout'),
]