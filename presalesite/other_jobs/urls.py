from django.urls import path, re_path
import re
from .views import Other_jobsListView, delete, final_list

urlpatterns = [
    path('', Other_jobsListView.as_view(), name='Other_jobs'),
    path('final/', final_list, name='Final_Other_jobs'),
    path('final/delete/', delete),
    path('delete/', delete),
]