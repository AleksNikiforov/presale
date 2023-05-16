from django import forms
from .models import *


class SubcontractorForm(forms.ModelForm):

    name = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'placeholder': 'Наименование','class': 'form-control'}))

    class Meta:
        #model = Subcontractor
        fields = '__all__'
        #fields = ('name', 'foods')


class CustomForm(forms.ModelForm):
    input = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Наименование подрядчика', 'title': '' }),
        help_text='',
    )

    class Meta:
        fields = '__all__'
