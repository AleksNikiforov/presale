from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Subcontractor_new
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin


''' 
    Здесь мы используем класс LoginRequiredMixin в качестве декоратора на уровне класса,
    чтобы проверить, авторизован ли пользователь. 
    Метод dispatch вызывается перед вызовом любого метода запроса (get, post, и т.д.) 
    и здесь мы просто вызываем метод dispatch родительского класса, 
    чтобы обеспечить правильное выполнение предварительной обработки запроса.
'''


class Subcontractor_newListView(LoginRequiredMixin, ListView):
    login_url = '/registration/login/'
    model = Subcontractor_new
    form_class = CustomForm


class Subcontractor_newUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/registration/login/'
    model = Subcontractor_new
    form_class = CustomForm
    success_url = '/subcontractor_new/'


class Subcontractor_newCreateView(LoginRequiredMixin, CreateView):
    login_url = '/registration/login/'
    model = Subcontractor_new
    form_class = CustomForm
    success_url = '/subcontractor_new/'


class Subcontractor_newDeleteView(LoginRequiredMixin, DeleteView):
    model = Subcontractor_new
    success_url = '/subcontractor_new/'