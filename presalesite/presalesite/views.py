from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required



@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'presalesite/index.html')