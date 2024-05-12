from django.conf import settings
import os
from PIL import Image
from django.db import models
from django.utils.text import slugify
from utils import utils


class Animal(models.Model):
    
    nome = models.CharField(max_length=255)
    dono = models.CharField(max_length=255, default='')
    raca_pet = models.CharField(max_length=255, default='')
    CHOICES = (
        ('macho', 'Macho'),
        ('fêmea', 'Fêmea'),
    )
    sexo = models.CharField(max_length=10, choices=CHOICES, default='')
    categoria_pet = models.CharField(max_length=255, default='')
    peso = models.CharField(max_length=255, default='')
    altura = models.CharField(max_length=255, default='')
    cor_pet = models.CharField(max_length=255, default='')
    vacinas_pet = models.TextField(default='')
    motivo_entrada_pet = models.CharField(max_length=255, default='')
    CHOICES1 = (
        ('retirada', 'Retirada'),
        ('à domicilio', 'À domicilio'),
        ('não se aplica', 'Não se aplica'),
    )
    tipo_entrega = models.CharField(max_length=20, choices=CHOICES1, default='')
    imagem = models.ImageField(
        upload_to='animal_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)


    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        


class Dono(models.Model):
    
    dono = models.CharField(max_length=50, blank=True, null=True)
    contato = models.CharField(max_length=11, blank=True, null=True)
    CPF = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.dono or self.animal.dono

    class Meta:
        verbose_name = 'Dono'
        verbose_name_plural = 'Donos'
