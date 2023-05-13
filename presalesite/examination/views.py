from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

''' 
    Здесь мы используем класс LoginRequiredMixin в качестве декоратора на уровне класса,
    чтобы проверить, авторизован ли пользователь. 
    Метод dispatch вызывается перед вызовом любого метода запроса (get, post, и т.д.) 
    и здесь мы просто вызываем метод dispatch родительского класса, 
    чтобы обеспечить правильное выполнение предварительной обработки запроса.
'''

class ExaminationListView(LoginRequiredMixin, ListView):
    login_url = '/registration/login/'
    model = Examination
    form_class = ExaminationForm

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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
                author = request.user                                                          # добавляем записи в БД
                name = n[0]
                days = n[1]
                if days:
                    cat = Examination(name = name, days = days, author = author)
                    cat.save()
                else:
                    cat = Examination(name = name, author = author)
                    cat.save()   
            return redirect(reverse_lazy('Final_Examination'))


def final_list(request):
    perechen = Examination.objects.filter(author=request.user)
    print(perechen)
    return render(request, 'examination/examination_final.html', {'perechen': perechen})


def delete(request):
    Examination.objects.filter(author=request.user).delete()
    return redirect(reverse_lazy('Examination'))

