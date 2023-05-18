from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
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

class BusinessTripListView(LoginRequiredMixin, ListView):
    login_url = '/registration/login/'
    model = BusinessTrip
    form_class = BusinessTripForm


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            data = dict(data)
            data.pop("csrfmiddlewaretoken")  
            duration_trip = int(round(float(data['Количество дней в командировке'][0]), 2))
            ticket_cost = int(round(float(data['Стоимость билетов, руб.'][0]), 2))
            hotel_cost = int(round(float(data['Стоимость гостиницы, руб.'][0]), 2))
            daily_allowance = int(round(float(data['Норма суточных, руб.'][0]), 2))          
            total_cost = (duration_trip * daily_allowance) + (duration_trip * hotel_cost) + ticket_cost
            BusinessTrip.objects.filter(author=request.user).delete()
            cat = BusinessTrip(author = request.user,
                        duration_trip = data['Количество дней в командировке'][0], 
                        ticket_cost = data['Стоимость билетов, руб.'][0], 
                        hotel_cost = data['Стоимость гостиницы, руб.'][0],
                        daily_allowance = data['Норма суточных, руб.'][0],
                        total_cost = total_cost,)
            cat.save()
            return redirect(reverse_lazy('Final_BusinessTrip'))


def final_list(request):
    perechen = BusinessTrip.objects.filter(author=request.user)
    return render(request, 'businesstrip/businesstrip_final.html', {'perechen': perechen})


def delete(request):
    BusinessTrip.objects.filter(author=request.user).delete()
    return redirect(reverse_lazy('BusinessTrip'))