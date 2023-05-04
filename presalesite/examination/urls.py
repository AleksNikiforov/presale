from django.urls import path, re_path
import re
from .views import ExaminationListView, delete, final_list

urlpatterns = [
    path('', ExaminationListView.as_view(), name='Examination'),
    path('final/', final_list, name='Final_Examination'),
    path('final/delete/', delete),
    path('delete/', delete),
]