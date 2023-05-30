from django.urls import path, re_path
import re
from .views import SubcontractorListView, SubcontractorCreateView, SubcontractorUpdateView, SubcontractorDeleteView

urlpatterns = [
    path('', SubcontractorListView.as_view(), name='Subcontractor'),
    path('subcontractor-update/', SubcontractorUpdateView.as_view()),
    path('subcontractor-create/', SubcontractorCreateView.as_view(), name='create_subcontractor'),
    path('subcontractor-update/<int:pk>/', SubcontractorUpdateView.as_view(), name='update_subcontractor'),
    path('subcontractor-delete/<int:pk>/', SubcontractorDeleteView.as_view(), name='delete_subcontractor'),
]