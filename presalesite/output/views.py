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
    #получение всех значений занесенных в таблицы
    design = Design.objects.all()
    examination = Examination.objects.all()
    poc = Poc.objects.all()
    rates = Rates.objects.all()
    #создание списка по которому пойдет цикл для отображения всех введенных данных
    all_fields = [design, examination, poc]
    #создание переменных для общей суммы
    all_person_days = 0
    all_tech_writer_days = 0
    all_manager_days = 0
    all_summa_s_nds = 0
    all_duration = 0


    number_of_paragraph = 1

    tech_writer_coef = Rates.objects.values('tech_writer_coef')
    tech_writer_coef = tech_writer_coef.values('tech_writer_coef')[0]['tech_writer_coef']
    tech_writer_cost = Rates.objects.values('tech_writer_cost')[0]['tech_writer_cost']
    manager_coef = Rates.objects.values('manager_coef')
    manager_coef = manager_coef.values('manager_coef')[0]['manager_coef']
    manager_cost = Rates.objects.values('manager_cost')[0]['manager_cost']
    person = rates.values('person')[0]['person']
    person_cost = Rates.objects.values('engineer_cost')[0]['engineer_cost'] if person == 'Инженер' else Rates.objects.values('architect_cost')[0]['architect_cost']

    perechen = [] 

    for data in all_fields:
        if data:
            #преобразование QuerySet в списко
            data = list(data.values('name', 'days'))
            #подготовка к расчету суммы с НДС, берем стоимость инженер/архитектор, техпис, менеджер и умножаем на количество рабочих дней
            person_days = data[0]['days']
            tech_writer_days = round(tech_writer_coef * person_days, 1)
            manager_days = round(manager_coef * person_days, 1)
            summa_s_nds = (person_cost * person_days + tech_writer_cost * tech_writer_days + manager_cost * manager_days) * 1.2
            #длительность проекта
            duration = person_days * 150 / 100
            #добавляем все данные в список для передачи в html
            data[0].update({'tech_writer_days': tech_writer_days})
            data[0].update({'manager_days': manager_days})
            data[0].update({'number': number_of_paragraph})
            data[0].update({'duration': duration})
            data[0].update({'summa_s_nds': summa_s_nds})
            data[0].update({'person': person})
            # № п/п
            number_of_paragraph += 1
            perechen.append(data)

            #делаем расчет общей суммы
            all_person_days += person_days
            all_tech_writer_days += tech_writer_days
            all_manager_days += manager_days
            all_summa_s_nds += summa_s_nds
            all_duration += duration


    itogo = [{'name': 'Итого:',
              'days': round(all_person_days, 1),
              'tech_writer_days': round(all_tech_writer_days, 1),
              'manager_days': round(all_manager_days,1),
              'duration': round(all_duration,1),
              'summa_s_nds': round(all_summa_s_nds,1)}]
    perechen.append(itogo)


    return render(request, 'output/output_final.html', {'perechen': perechen})
