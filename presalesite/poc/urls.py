from django.urls import path, re_path
import re
from .views import PocListView, delete, final_list

urlpatterns = [
    path('', PocListView.as_view(), name='Poc'),
    path('final/', final_list, name='Final_Poc'),
    path('final/delete/', delete),
    path('delete/', delete),
]