from django.urls import path, re_path
import re
from .views import final_list

urlpatterns = [
    # path('', OutputListView.as_view(), name='Output'),
    path('', final_list, name='Output'),
    # path('final/delete/', delete),
    # path('delete/', delete),
]