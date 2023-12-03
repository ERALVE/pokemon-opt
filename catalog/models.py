from django.db import models

# Create your models here.
class Catalog(models.Model):
    nombre = models.CharField(max_length=25, default= '')
    edad = models.IntegerField(default= 0)
    pais = models.CharField(max_length=27, default= '')
    dni = models.CharField(max_length=8, default= '00000000')
    vigente = models.BooleanField(default=True)