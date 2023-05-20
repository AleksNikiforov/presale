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


class Other_jobsListView(LoginRequiredMixin, ListView):
    login_url = '/registration/login/'
    model = Other_jobs
    form_class = Other_jobsForm

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        # Fetch the Accept associated with the current user
        other_jobs = Other_jobs.objects.filter(author=request.user)
        
        if other_jobs.exists():
            # Other_jobs exist, pass them to the template context
            names = other_jobs.values_list('name', flat=True)
            context = {'other_jobs': other_jobs, 'names': names}
            return render(request, 'other_jobs/other_jobs_list.html', context)
        else:
            # No Other_jobs exist, render the fallback template
            return render(request, 'other_jobs/other_jobs_list.html')
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            data = {k: v for k, v in data.items() if v is not None and v != ""}            # удаляем лишние поля из словаря
            data.pop("csrfmiddlewaretoken")                                                # удаляем лишние поля из словаря
            data = {key: value for key, value in data.items() if key != value}             # удаляем лишние поля из словаря
            checked = data['checked_items'].split(',')                                     # разделяем checked_items и создаем список из его значений
            data.pop("checked_items")      
            Other_jobs.objects.filter(author=request.user).delete()                                               
            for item in checked:                                                           # значениям на против которые стоят галочки ставим значение клоичества дней Null
                data[item] = None
            for n in data.items():   
                author = request.user                                                      # добавляем записи в БД
                name = n[0]
                days = n[1]
                if days:
                    cat = Other_jobs(name = name, days = days, author = author)
                    cat.save()
                else:
                    cat = Other_jobs(name = name, author = author)
                    cat.save()   
            return redirect(reverse_lazy('Final_Other_jobs'))


def final_list(request):
    perechen = Other_jobs.objects.filter(author=request.user)
    return render(request, 'other_jobs/other_jobs_final.html', {'perechen': perechen})


def delete(request):
    Other_jobs.objects.filter(author=request.user).delete()
    return redirect(reverse_lazy('Other_jobs'))

