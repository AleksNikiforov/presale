from django import forms
from .models import *


class Other_jobsForm(forms.ModelForm):

    name = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'placeholder': 'Наименование','class': 'form-control'}))

    class Meta:
        #model = Other_jobs
        fields = '__all__'
        #fields = ('name', 'foods')
