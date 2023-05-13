from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import *
from .forms import *



class RatesListView(ListView):
    model = Rates
    form_class = RatesForm
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            data = dict(data)
            data.pop("csrfmiddlewaretoken")  
            person = data['checked_items'][0]
            ''' Если отмечаем Архитектор то получается ключ со значением Архитектор и стоимостью, аналогично для Инженера
            {'Архитектор': ['Архитектор', '25400.00'],
              'Инженер': ['20400.00'],
              'Менеджер проекта': ['20400.00'],
              'Разработчик технической документации': ['16400.00'],
              'Менеджер проекта коэффициент': ['0.3'],
              'Разработчик технической документации коэффициент': ['0.3'],
              'checked_items': ['Архитектор']}
              Поэтому нужно делать проверку и вставлять соответствующее значение
              '''
            default_num_engineer = 0
            default_num_architect = 0
            if person == 'Архитектор':
                default_num_architect = -1
            if person == 'Инженер':
                default_num_engineer = -1
            Rates.objects.filter(author=request.user).delete()
            cat = Rates(author = request.user,
                        person = person,
                        engineer_cost = data['Инженер'][default_num_engineer], 
                        architect_cost = data['Архитектор'][default_num_architect], 
                        manager_cost = data['Менеджер проекта'][0],
                        tech_writer_cost = data['Разработчик технической документации'][0],
                        manager_coef = data['Менеджер проекта коэффициент'][0],
                        tech_writer_coef = data['Разработчик технической документации коэффициент'][0])
            cat.save()
            return redirect(reverse_lazy('Final_Rates'))


def final_list(request):
    perechen = Rates.objects.filter(author=request.user)
    return render(request, 'rates/rates_final.html', {'perechen': perechen})


def delete(request):
    Rates.objects.filter(author=request.user).delete()
    return redirect(reverse_lazy('Rates'))