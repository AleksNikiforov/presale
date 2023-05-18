from django.urls import path, re_path
import re
from .views import BusinessTripListView, delete, final_list

urlpatterns = [
    path('', BusinessTripListView.as_view(), name='BusinessTrip'),
    path('final/', final_list, name='Final_BusinessTrip'),
    path('final/delete/', delete),
    path('delete/', delete),
]