from django import forms

class CalculoImc(forms.Form):
  peso = forms.FloatField()
  altura = forms.FloatField()