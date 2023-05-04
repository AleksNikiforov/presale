from django.urls import path, re_path
import re
from .views import RatesListView, delete, final_list

urlpatterns = [
    path('', RatesListView.as_view(), name='Rates'),
    path('final/', final_list, name='Final_Rates'),
    path('final/delete/', delete),
    path('delete/', delete),
]