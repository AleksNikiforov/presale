from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from design.models import Design
from examination.models import Examination
from poc.models import Poc
from rates.models import Rates
from .models import Output
from .forms import *


def final_list(request):

    design = Design.objects.all()
    examination = Examination.objects.all()
    poc = Poc.objects.all()
    rates = Rates.objects.all()
    print('='*50)
    print(design)
    print('='*50)
    print(examination)
    print('='*50)
    print(poc)
    print('='*50)
    print(rates)
    print('='*50)
    perechen = [design, examination, poc, rates]

    duration_design = Design.objects.values('name', 'days')
    print('0'*50)
    print(duration_design)
    print('0'*50)
    person = Rates.objects.values('person')
    engineer_cost = Rates.objects.values('engineer_cost')
    architect_cost = Rates.objects.values('architect_cost')
    manager_cost = Rates.objects.values('manager_cost')
    manager_coef = Rates.objects.values('manager_coef')
    tech_writer_cost = Rates.objects.values('tech_writer_cost')
    tech_writer_coef = Rates.objects.values('tech_writer_coef')
    print('0'*50)
    print(person, engineer_cost, architect_cost, manager_cost, manager_coef, tech_writer_cost, tech_writer_coef)

    duration_design = Design.objects.values('days')
    print('0'*50)
    print(duration_design)


    my_queryset = Design.objects.exclude(days=None)
    days_list = my_queryset.values_list('days', flat=True)
    my_value = days_list.first()
    print('0'*50)
    print(my_value)



    return render(request, 'output/output_final.html', {'perechen': perechen})



# class OutputListView(ListView):
#     model = Output
#     form_class = OutputForm
#     design = Design.objects.all()
#     examination = Examination.objects.all()
#     poc = Poc.objects.all()
#     print('='*50)
#     print(design)
#     print('='*50)
#     print(examination)
#     print('='*50)
#     print(poc)
#     print('='*50)
#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             data = request.POST
#             data = {k: v for k, v in data.items() if v is not None and v != ""}            # удаляем лишние поля из словаря
#             data.pop("csrfmiddlewaretoken")                                                # удаляем лишние поля из словаря
#             data = {key: value for key, value in data.items() if key != value}             # удаляем лишние поля из словаря
#             checked = data['checked_items'].split(',')                                     # разделяем checked_items и создаем список из его значений
#             data.pop("checked_items")                                                      # удаляем checked_items из словаря
#             for item in checked:                                                           # значениям на против которые стоят галочки ставим значение клоичества дней Null
#                 data[item] = None
#             for n in data.items():                                                         # добавляем записи в БД
#                 name = n[0]
#                 days = n[1]
#                 if days:
#                     cat = Examination(name = name, days = days)
#                     cat.save()
#                 else:
#                     cat = Examination(name = name)
#                     cat.save()   
#             return redirect(reverse_lazy('Final_Examination'))





# def delete(request):
#     Examination.objects.all().delete()
#     return redirect(reverse_lazy('Examination'))

