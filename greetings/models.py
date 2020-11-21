from django.db import models


# Create your models here.

class Greeting(models.Model):
    name = models.TextField()
    surname = models.TextField()

    greeting = models.TextField()

class Dario(models.Model):
    dataMovimento = models.DateField()
    causale = models.TextField()
    importo = models.IntegerField()
    idutente = models.TextField()
