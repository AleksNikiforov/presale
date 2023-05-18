from django import forms
from .models import *


class BusinessTripForm(forms.ModelForm):

    name = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'placeholder': 'Наименование','class': 'form-control'}))

    class Meta:
        #model = BusinessTrip
        fields = '__all__'
        #fields = ('name', 'foods')
