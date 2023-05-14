from django import forms
from .models import *


class CommissioningForm(forms.ModelForm):

    name = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'placeholder': 'Наименование','class': 'form-control'}))

    class Meta:
        #model = Commissioning
        fields = '__all__'
        #fields = ('name', 'foods')
