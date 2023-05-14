from django.urls import path, re_path
import re
from .views import CommissioningListView, delete, final_list

urlpatterns = [
    path('', CommissioningListView.as_view(), name='Commissioning'),
    path('final/', final_list, name='Final_Commissioning'),
    path('final/delete/', delete),
    path('delete/', delete),
]