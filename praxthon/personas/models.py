from django.db import models


# Create your models here.

class Persona (models.Model):
    nombre      = models.CharField(max_length=255)
    telefono    = models.CharField(max_length=255)
    # correo      = models.CharField(max_length=255)
    correo      = models.EmailField(max_length=254)
    perfil      = models.CharField(max_length=255)
    habilidades = models.CharField(max_length=255)


    def __str__(self):
        return f'Persona {self.id}: {self.nombre}, Tel.: {self.telefono}, Email: {self.correo}'


