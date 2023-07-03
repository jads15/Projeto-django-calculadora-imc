from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView 
from calculo_imc.forms import CalculoImc

# Create your views here.

class Home(TemplateView,FormView):
  template_name = 'home.html'
  form_class =CalculoImc
  
  def get_context_data(self, **kwargs):
   context = super().get_context_data(**kwargs)
   context['form'] = self.form_class
   return context
  
  def form_valid(self, form):
   peso = form.cleaned_data['peso']
   altura = form.cleaned_data['altura']
   imc = (peso)/(altura**2)
   if imc >= 18.5 and imc < 25:
    return HttpResponse(f'imc: {imc:.2f}  Peso normal' )
   elif imc >= 25 and imc < 30:
    return HttpResponse(f'imc: {imc:.2f}  Sobrepeso' )
   elif imc >=30 and imc < 35:
    return HttpResponse(f'imc: {imc:.2f}  Obesidade grau I' )
   elif imc >=35 and imc < 40:
    return HttpResponse(f'imc: {imc:.2f} Obesidade grau II' )
   elif imc >=40:
    return HttpResponse(f'imc: {imc:.2f} Obesidade grau III' )
   else:
    return HttpResponse(f'imc: {imc:2f} Abaixo do peso' )


