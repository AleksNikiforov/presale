from django.urls import path, re_path
import re
from .views import MigrationListView, delete, final_list

urlpatterns = [
    path('', MigrationListView.as_view(), name='Migration'),
    path('final/', final_list, name='Final_Migration'),
    path('final/delete/', delete),
    path('delete/', delete),
]