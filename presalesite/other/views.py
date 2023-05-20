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


class OtherListView(LoginRequiredMixin, ListView):
    login_url = '/registration/login/'
    model = Other
    form_class = OtherForm


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        # Fetch the Other associated with the current user
        other = Other.objects.filter(author=request.user)
        
        if other.exists():
            # Other exist, pass them to the template context
            total_price = other.values('total_price')
            context = {'total_price': total_price}
            return render(request, 'other/other_list.html', context)
        else:
            # No Other exist, render the fallback template
            return render(request, 'other/other_list.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            data = dict(data)
            data.pop("csrfmiddlewaretoken")  
            Other.objects.filter(author=request.user).delete()
            cat = Other(author = request.user,
                        total_price = data['Общая стоимость расходных материалов'][0], 
                        )
            cat.save()
            return redirect(reverse_lazy('Final_Other'))


def final_list(request):
    perechen = Other.objects.filter(author=request.user)
    return render(request, 'other/other_final.html', {'perechen': perechen})


def delete(request):
    Other.objects.filter(author=request.user).delete()
    return redirect(reverse_lazy('Other'))

