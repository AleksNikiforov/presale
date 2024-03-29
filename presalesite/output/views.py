from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from design.models import Design
from examination.models import Examination
from poc.models import Poc
from rates.models import Rates
from install.models import Install
from commissioning.models import Commissioning
from accept.models import Accept
from migration.models import Migration
from other_jobs.models import Other_jobs
from subcontractor.models import Subcontractor
from other.models import Other
from businesstrip.models import BusinessTrip
from .forms import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def delete_all(request):

    Design.objects.filter(author=request.user).delete()
    Examination.objects.filter(author=request.user).delete()
    Poc.objects.filter(author=request.user).delete()
    Rates.objects.filter(author=request.user).delete()
    Install.objects.filter(author=request.user).delete()
    Commissioning.objects.filter(author=request.user).delete()
    Accept.objects.filter(author=request.user).delete()
    Migration.objects.filter(author=request.user).delete()
    Other_jobs.objects.filter(author=request.user).delete()
    Subcontractor.objects.filter(author=request.user).delete()
    Other.objects.filter(author=request.user).delete()
    BusinessTrip.objects.filter(author=request.user).delete()

    message = "Все записи успешно удалены"
    messages.success(request, message)
    return redirect('Home')


@login_required(login_url=settings.LOGIN_URL)
def final_list(request):
    #получение всех значений занесенных в таблицы
    design = Design.objects.filter(author=request.user)
    examination = Examination.objects.filter(author=request.user)
    poc = Poc.objects.filter(author=request.user)
    rates = Rates.objects.filter(author=request.user)
    install = Install.objects.filter(author=request.user)
    commissioning = Commissioning.objects.filter(author=request.user)
    accept = Accept.objects.filter(author=request.user)
    migration = Migration.objects.filter(author=request.user)
    other_jobs = Other_jobs.objects.filter(author=request.user)
    subcontractor = Subcontractor.objects.filter(author=request.user)
    other = Other.objects.filter(author=request.user)
    businesstrip = BusinessTrip.objects.filter(author=request.user)
    #создание списка по которому пойдет цикл для отображения всех введенных данных
    all_fields = [design, examination, poc, install, commissioning, accept, migration, other_jobs, subcontractor, other, businesstrip]
    #создание переменных для общей суммы
    all_person_days = 0
    all_tech_writer_days = 0
    all_manager_days = 0
    all_summa_s_nds = 0
    all_duration = 0
    number_of_paragraph = 1
    #проверяем заполнены ли Rates, если при обращении к Rates выходит ошибка, перенаправляем на форму для заполнения Rates
    try:
        tech_writer_coef = Rates.objects.filter(author=request.user).values('tech_writer_coef')
        tech_writer_coef = tech_writer_coef.values('tech_writer_coef')[0]['tech_writer_coef']
        tech_writer_cost = Rates.objects.filter(author=request.user).values('tech_writer_cost')[0]['tech_writer_cost']
        manager_coef = Rates.objects.filter(author=request.user).values('manager_coef')
        manager_coef = manager_coef.values('manager_coef')[0]['manager_coef']
        manager_cost = Rates.objects.filter(author=request.user).values('manager_cost')[0]['manager_cost']
        person = rates.values('person')[0]['person']
        person_cost = Rates.objects.filter(author=request.user).values('engineer_cost')[0]['engineer_cost'] if person == 'Инженер' else Rates.objects.filter(author=request.user).values('architect_cost')[0]['architect_cost']
    except Exception as e:
        return redirect('Rates')
    
    perechen = [] 

    for data in all_fields:
        if data:
            #преобразование QuerySet в список
            data = list(data.values())
            #проверяем есть ли подрядчик, с ним работает отдельно, отдельная строка
            key_of_subcontractor = data[0].get('subcontract_name')
            key_of_other = data[0].get('total_price')
            key_of_businesstrip = data[0].get('daily_allowance')
            if key_of_other:
                data[0].update({'number': number_of_paragraph})
                data[0].update({'name': 'Прочие расходы (Монтажный комплект)'})
                data[0].update({'total_price': data[0].get('total_price')})
                number_of_paragraph += 1
                perechen.append(data)
                all_summa_s_nds += data[0].get('total_price')
            elif key_of_subcontractor:
                data[0].update({'number': number_of_paragraph})
                data[0].update({'subcontract_name': data[0].get('subcontract_name')})
                data[0].update({'subcontract_jobs': data[0].get('subcontract_jobs')})
                data[0].update({'subcontract_price': data[0].get('subcontract_price')})
                number_of_paragraph += 1
                perechen.append(data)
                all_summa_s_nds += data[0].get('subcontract_price')
            elif key_of_businesstrip:
                data[0].update({'number': number_of_paragraph})
                data[0].update({'name': 'Командировочные расходы'})
                data[0].update({'total_price': data[0].get('total_cost')})
                number_of_paragraph += 1
                perechen.append(data)
                all_summa_s_nds += data[0].get('total_cost')
            else:
                person_days = data[0]['days']
                #технический писатель учитывется только в работах указанных в списке, в других типах работ он не учитывается
                tech_writer_days = 0
                allowed_values = [  
                                    'Проектно-изыскательские работы',
                                    'Проектно-изыскательские работы (Предпроектная стадия)',
                                    'Проектно-изыскательские работы (Проектная стадия) (ГОСТ 34)',
                                    'Проектно-изыскательские работы (ГОСТ 21)',
                                    'Проектно-изыскательские работы (Сокращенная версия)',
                                    'Разработка плана миграции (пользовательский сегмент)',
                                    'Разработка плана миграции (серверный сегмент)',
                                    'Разработка плана миграции (МСЭ сегмент)',
                                    'Разработка отчета о текущем состоянии:',
                                    'Разработка программы испытания решения',
                                    'Разработка рекомендаций по устранению выявленных недостков:',
                                    'Разработка рекомендаций по развитию сети:',
                                    'Разработка плана миграции',
                                 ]
                rtd = False
                for int_dict in data:
                    if int_dict['name'] in allowed_values:
                        rtd = True
                if rtd:
                    tech_writer_days = round(tech_writer_coef * person_days, 1)
                #подготовка к расчету суммы с НДС, берем стоимость инженер/архитектор, техпис, менеджер и умножаем на количество рабочих дней
                manager_days = round(manager_coef * person_days, 1)
                #ндс суммарное считаем =1 а не 1.2 так как ндс учитывается в коэффициентах исполнителей
                summa_s_nds = (person_cost * person_days + tech_writer_cost * tech_writer_days + manager_cost * manager_days) * 1
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
              'summa_s_nds': round(all_summa_s_nds,1)}
              ]
    perechen.append(itogo)

    return render(request, 'output/output_final.html', {'perechen': perechen})
