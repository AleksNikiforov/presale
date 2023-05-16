from django.urls import path, re_path
import re
from .views import SubcontractorListView, delete, final_list

urlpatterns = [
    path('', SubcontractorListView.as_view(), name='Subcontractor'),
    path('final/', final_list, name='Final_Subcontractor'),
    path('final/delete/', delete),
    path('delete/', delete),
]