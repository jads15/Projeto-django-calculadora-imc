from django.test import TestCase
from django.urls import reverse
from calculo_imc.views import Home
from calculo_imc.forms import CalculoImc
# Create your tests here.
class Test(TestCase):
  def testar_requisição(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code,200)
  
  def testar_formulário(self):
    dados = {'peso':80,'altura':1.90}
    formulario = CalculoImc(data = dados)
    self.assertFalse(formulario.is_valid())