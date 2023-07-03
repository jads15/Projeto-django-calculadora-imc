from django.contrib import admin
from django.urls import path
from calculo_imc.views import Home

urlpatterns = [
    path('', Home.as_view() ,name = 'home') ,
]
