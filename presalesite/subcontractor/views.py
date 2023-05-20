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


class SubcontractorListView(LoginRequiredMixin, ListView):
    login_url = '/registration/login/'
    model = Subcontractor
    form_class = CustomForm


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        # Fetch the Subcontractor associated with the current user
        subcontractors = Subcontractor.objects.filter(author=request.user)
        
        if subcontractors.exists():
            # Subcontractor exist, pass them to the template context
            subcontractor_name = subcontractors.values('subcontract_name')
            subcontractor_jobs = subcontractors.values('subcontract_jobs')
            subcontractor_price = subcontractors.values('subcontract_price')
            context = {'subcontractor_name': subcontractor_name, 'subcontractor_jobs':subcontractor_jobs, 'subcontractor_price':subcontractor_price}
            return render(request, 'subcontractor/subcontractor_list.html', context)
        else:
            # No Subcontractor exist, render the fallback template
            return render(request, 'subcontractor/subcontractor_list.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            data = dict(data)
            data.pop("csrfmiddlewaretoken")  
            Subcontractor.objects.filter(author=request.user).delete()
            cat = Subcontractor(author = request.user,
                        subcontract_name = data['Наименование подрядчика'][0], 
                        subcontract_jobs = data['Наименование работ'][0], 
                        subcontract_price = data['Стоимость'][0],
                        )
            cat.save()
            return redirect(reverse_lazy('Final_Subcontractor'))


def final_list(request):
    perechen = Subcontractor.objects.filter(author=request.user)
    return render(request, 'subcontractor/subcontractor_final.html', {'perechen': perechen})


def delete(request):
    Subcontractor.objects.filter(author=request.user).delete()
    return redirect(reverse_lazy('Subcontractor'))

