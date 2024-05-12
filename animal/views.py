from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

from . import models
from perfil.models import Perfil


class ListaAnimals(ListView):
    model = models.Animal
    template_name = 'animal/lista.html'
    context_object_name = 'animals'
    paginate_by = 10
    ordering = ['-id']


class Busca(ListaAnimals):
    def get_queryset(self, *args, **kwargs):
        termo = self.request.GET.get('termo') or self.request.session['termo']
        qs = super().get_queryset(*args, **kwargs)

        if not termo:
            return qs

        self.request.session['termo'] = termo

        qs = qs.filter(
            Q(nome__icontains=termo) |
            Q(raca_pet__icontains=termo) |
            Q(peso__icontains=termo) 
            
        )

        self.request.session.save()
        return qs


class DetalheAnimal(DetailView):
    model = models.Animal
    template_name = 'animal/detalhe.html'
    context_object_name = 'animal'
    slug_url_kwarg = 'slug'


