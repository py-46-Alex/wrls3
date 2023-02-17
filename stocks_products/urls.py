"""stocks_products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    hte include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import datetime
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

def time_view(request):
    current_data = datetime.date.today()
    cur_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_data} , {cur_time}'
    return HttpResponse(msg)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('logistic.urls')),
    path('', time_view, name='home')
]
