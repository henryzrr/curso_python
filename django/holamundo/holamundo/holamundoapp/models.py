from django.db import models

# Create your models here.
class Computadora(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
