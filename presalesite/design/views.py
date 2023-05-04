from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import *
from .forms import *



class DesignListView(ListView):
    model = Design
    form_class = DesignForm
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
                    cat = Design(name = name, days = days)
                    cat.save()
                else:
                    cat = Design(name = name)
                    cat.save()   
            return redirect(reverse_lazy('Final_Design'))


def final_list(request):
    perechen = Design.objects.all()
    return render(request, 'design/design_final.html', {'perechen': perechen})


def delete(request):
    Design.objects.all().delete()
    return redirect(reverse_lazy('Design'))