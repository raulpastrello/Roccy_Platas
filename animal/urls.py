from django.urls import path
from . import views


app_name = 'animal'

urlpatterns = [
    path('', views.ListaAnimals.as_view(), name="lista"),
    path('<slug>', views.DetalheAnimal.as_view(), name="detalhe"),
    path('busca/', views.Busca.as_view(), name="busca"),
]
