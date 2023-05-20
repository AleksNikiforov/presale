from django.urls import path, re_path
import re
from .views import final_list, delete_all

urlpatterns = [
    # path('', OutputListView.as_view(), name='Output'),
    path('', final_list, name='Output'),
    path('delete_all/', delete_all),
    # path('delete/', delete),
]