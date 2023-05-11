from django.urls import path, re_path
from .views import InstallListView, delete, final_list

urlpatterns = [
    path('', InstallListView.as_view(), name='Install'),
    path('final/', final_list, name='Final_Install'),
    path('final/delete/', delete),
    path('delete/', delete),
]