from django import forms
from .models import *


class CustomForm(forms.ModelForm):
    class Meta:
        model = Subcontractor
        fields = ['subcontract_name', 'subcontract_jobs', 'subcontract_price']
        labels = {
            'subcontract_name': 'Наименование подрядчика',
            'subcontract_jobs': 'Наименование работ',
            'subcontract_price': 'Стоимость с НДС, руб',
        }
        widgets = {
            'subcontract_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'subcontract_jobs': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'subcontract_price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
        }