from django.db import models

# Create your models here.
class Coeficientes(models.Model):
    a = models.SmallIntegerField(blank=True, null=True)
    b = models.SmallIntegerField(blank=True, null=True)
    c = models.SmallIntegerField(blank=True, null=True)

def __strin__(self):
    return f"{resultado}"