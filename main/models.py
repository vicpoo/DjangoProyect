from django.db import models
from django.contrib.auth.models import User

class Universo(models.Model):
    """
    Modelo que representa un universo en el que existen Spider-Man y sus enemigos.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class SpiderMan(models.Model):
    """
    Modelo que representa una versión de Spider-Man.
    """
    nombre = models.CharField(max_length=100)
    universo = models.ForeignKey(Universo, on_delete=models.CASCADE, null=True, blank=True)  # Permitir nulos temporalmente
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Enemigo(models.Model):
    """
    Modelo que representa un enemigo de Spider-Man.
    """
    nombre = models.CharField(max_length=100)
    universo = models.ForeignKey(Universo, on_delete=models.CASCADE, null=True, blank=True)  # Permitir nulos temporalmente
    alias = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Batalla(models.Model):
    """
    Modelo que representa una batalla entre Spider-Man y un enemigo.
    """
    spider_man = models.ForeignKey(SpiderMan, on_delete=models.CASCADE)
    enemigo = models.ForeignKey(Enemigo, on_delete=models.CASCADE)
    fecha = models.DateField()
    resultado = models.CharField(max_length=100)

    def __str__(self):
        return f"{str(self.spider_man)} vs {str(self.enemigo)}"

class Comentario(models.Model):
    """
    Modelo que representa un comentario de un usuario sobre una batalla.
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    batalla = models.ForeignKey(Batalla, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {str(self.usuario.username)} en {str(self.batalla)}"