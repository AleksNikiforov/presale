from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Subcontractor
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


class SubcontractorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/registration/login/'
    model = Subcontractor
    form_class = CustomForm
    success_url = '/subcontractor/'


class SubcontractorCreateView(LoginRequiredMixin, CreateView):
    login_url = '/registration/login/'
    model = Subcontractor
    form_class = CustomForm
    success_url = '/subcontractor/'


class SubcontractorDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/registration/login/'
    model = Subcontractor
    success_url = '/subcontractor/'