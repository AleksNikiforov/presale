from django.urls import path, re_path
import re
from .views import AcceptListView, delete, final_list

urlpatterns = [
    path('', AcceptListView.as_view(), name='Accept'),
    path('final/', final_list, name='Final_Accept'),
    path('final/delete/', delete),
    path('delete/', delete),
]