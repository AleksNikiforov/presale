from django.urls import path, re_path
import re
from .views import Subcontractor_newListView, Subcontractor_newCreateView, Subcontractor_newUpdateView, Subcontractor_newDeleteView

urlpatterns = [
    path('', Subcontractor_newListView.as_view(), name='Subcontractor_new'),
    path('subcontractor_new-update/', Subcontractor_newUpdateView.as_view()),
    path('subcontractor_new-create/', Subcontractor_newCreateView.as_view(), name='create_subcontractor'),
    path('subcontractor_new-update/<int:pk>/', Subcontractor_newUpdateView.as_view(), name='update_subcontractor'),
    path('subcontractor_new-delete/<int:pk>/', Subcontractor_newDeleteView.as_view(), name='delete_subcontractor'),
]