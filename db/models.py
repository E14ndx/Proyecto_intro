from django.db import models

# Create your models here.

class usuarios(models.Model):
    nombre=models.CharField(max_length=25)
    contraseña=models.CharField(max_length=20)
    mail=models.EmailField()