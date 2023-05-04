from django.urls import path, re_path
import re
from .views import DesignListView, delete, final_list

urlpatterns = [
    path('', DesignListView.as_view(), name='Design'),
    path('final/', final_list, name='Final_Design'),
    path('final/delete/', delete),
    path('delete/', delete),
]