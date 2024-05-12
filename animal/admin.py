from django.contrib import admin
from . import models
from .forms import DonoForm
from .models import Dono
from .models import Animal
from .forms import AnimalForm

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    form = AnimalForm
    add_form = AnimalForm # It is not a native django field. I created this field and use it in get_form method.

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during foo creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)
    

@admin.register(Dono)
class FooAdmin(admin.ModelAdmin):
    form = DonoForm
    add_form = DonoForm # It is not a native django field. I created this field and use it in get_form method.

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during foo creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)