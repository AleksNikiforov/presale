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

    data = list(design.values('name', 'days'))


    number = 1

    person_days = data[0]['days']

    tech_writer_coef = Rates.objects.values('tech_writer_coef')
    tech_writer_coef = tech_writer_coef.values('tech_writer_coef')[0]['tech_writer_coef']
    tech_writer_days = tech_writer_coef * person_days

    manager_coef = Rates.objects.values('manager_coef')
    manager_coef = manager_coef.values('manager_coef')[0]['manager_coef']
    manager_days = manager_coef * person_days

    duration = person_days * 150 / 100

    #подготовка к расчету суммы с НДС, берем стоимость инженер/архитектор, техпис, менеджер и умножаем на количество рабочих дней
    tech_writer_cost = Rates.objects.values('tech_writer_cost')[0]['tech_writer_cost']
    manager_cost = Rates.objects.values('manager_cost')[0]['manager_cost']
    person = rates.values('person')[0]['person']
    if person == 'Инженер':
        person_cost = Rates.objects.values('engineer_cost')[0]['engineer_cost']
    else:
        person_cost = Rates.objects.values('architect_cost')[0]['architect_cost']
    summa_s_nds = (person_cost * person_days + tech_writer_cost * tech_writer_days + manager_cost * manager_days) * 1.2


    data[0].update({'tech_writer_days': tech_writer_days})
    data[0].update({'manager_days': manager_days})
    data[0].update({'number': number})
    data[0].update({'duration': duration})
    data[0].update({'summa_s_nds': summa_s_nds})
    data[0].update({'person': person})

    number =+ 1


    perechen = data

    print(perechen)




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

