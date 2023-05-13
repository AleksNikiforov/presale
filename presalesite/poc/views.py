from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import *
from .forms import *



class PocListView(ListView):
    model = Poc
    form_class = PocForm
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
            for n in data.items():   
                author = request.user                                                      # добавляем записи в БД
                name = n[0]
                days = n[1]
                if days:
                    cat = Poc(name = name, days = days, author = author)
                    cat.save()
                else:
                    cat = Poc(name = name, author = author)
                    cat.save()   
            return redirect(reverse_lazy('Final_Poc'))


def final_list(request):
    perechen = Poc.objects.filter(author=request.user)
    return render(request, 'poc/poc_final.html', {'perechen': perechen})


def delete(request):
    Poc.objects.filter(author=request.user).delete()
    return redirect(reverse_lazy('Poc'))

