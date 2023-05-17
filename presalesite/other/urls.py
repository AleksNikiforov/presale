from django.urls import path, re_path
import re
from .views import OtherListView, delete, final_list

urlpatterns = [
    path('', OtherListView.as_view(), name='Other'),
    path('final/', final_list, name='Final_Other'),
    path('final/delete/', delete),
    path('delete/', delete),
]