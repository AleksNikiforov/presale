from django import forms
from .models import *


class CustomForm(forms.ModelForm):
    class Meta:
        model = Subcontractor_new
        fields = ['subcontract_name', 'subcontract_jobs', 'subcontract_price']
        labels = {
            'subcontract_name': 'Наименование подрядчика',
            'subcontract_jobs': 'Наименование работ',
            'subcontract_price': 'Стоимость работ',
        }
        widgets = {
            'subcontract_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subcontract_jobs': forms.TextInput(attrs={'class': 'form-control'}),
            'subcontract_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
