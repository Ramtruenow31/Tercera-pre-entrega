from django.db import models
class Pelicula(models.Model):
    titulo = models.CharField(max_length=40)
    genero = models.IntegerField(unique=True)
    def __str__(self):
        return f"{self.titulo}, genero: {self.genero}"

class Musica(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}, genero: {self.genero}"

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.marca}, color {self.color}"