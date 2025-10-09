from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Requerimiento(models.Model):
    id_rf = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200, unique=True, null=True, blank=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, blank=True, related_name='requerimientos')
    satisfaccion = models.IntegerField()
    necesidad = models.IntegerField()
    tecnica = models.IntegerField()
    dependencia = models.IntegerField()
    prioridad = models.IntegerField(default=0)
    resultado = models.FloatField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id_rf} - {self.resultado}"
