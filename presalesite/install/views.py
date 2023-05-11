from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import *
from .forms import *



class InstallListView(ListView):
    model = Install
    form_class = InstallForm
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            data = {k: v for k, v in data.items() if v is not None and v != ""}            # удаляем лишние поля из словаря
            data.pop("csrfmiddlewaretoken")                                                # удаляем лишние поля из словаря
            data = {key: value for key, value in data.items() if key != value}             # удаляем лишние поля из словаря
            checked = data['checked_items'].split(',')                                     # разделяем checked_items и создаем список из его значений
            data.pop("checked_items")                                                      # удаляем checked_items из словаря
            for item in checked:                                                           # значениям на против которые стоят галочки ставим значение клоичества дней Null
                data[item] = None
            for n in data.items():                                                         # добавляем записи в БД
                name = n[0]
                days = n[1]
                if days:
                    cat = Install(name = name, days = days)
                    cat.save()
                else:
                    cat = Install(name = name)
                    cat.save()   
            return redirect(reverse_lazy('Final_Install'))


def final_list(request):
    perechen = Install.objects.all()
    print(perechen)
    return render(request, 'install/install_final.html', {'perechen': perechen})


def delete(request):
    Install.objects.all().delete()
    return redirect(reverse_lazy('Install'))

