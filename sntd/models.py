from django.db import models

class Requerimiento(models.Model):
    id_rf = models.CharField(max_length=50, unique=True)
    satisfaccion = models.IntegerField()
    necesidad = models.IntegerField()
    tecnica = models.IntegerField()
    dependencia = models.IntegerField()
    resultado = models.FloatField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id_rf} - {self.resultado}"
