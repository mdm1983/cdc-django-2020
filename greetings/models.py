from django.db import models


# Create your models here.

class Greeting(models.Model):
    name = models.TextField()
    surname = models.TextField()

    greeting = models.TextField()

class MovimentoOne(models.Model):
    datamov = models.DateTimeField()
    causale = models.TextField()
    importo = models.IntegerField()
    email = models.TextField()

