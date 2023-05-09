from django.urls import path, re_path
import re
from .views import register_view, login_view

urlpatterns = [
    path('', register_view, name='Registration'),
    path('login/', login_view, name='Login'),
]