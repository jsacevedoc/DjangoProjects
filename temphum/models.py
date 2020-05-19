from django.db import models
import uuid

class Temphum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Cultivo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(verbose_name='Codigo', max_length=20)
    latitud = models.CharField(verbose_name='Latidud', max_length=20)
    longitud = models.CharField(verbose_name='Longitud', max_length=20)
    producto = models.CharField(verbose_name='Producto', max_length=25)
    area = models.IntegerField(verbose_name='Area')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 