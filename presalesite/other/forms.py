from django import forms
from .models import *


class OtherForm(forms.ModelForm):

    name = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'placeholder': 'Наименование','class': 'form-control'}))

    class Meta:
        #model = Other
        fields = '__all__'
        #fields = ('name', 'foods')

