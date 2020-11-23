from django.db import models


# Create your models here.

class Greeting(models.Model):
    name = models.TextField()
    surname = models.TextField()

    greeting = models.TextField()

class MovimentoOne(models.Model):
    datamov = models.DateField()
    causale = models.TextField()
    importo = models.IntegerField()
    email = models.TextField()

class MovimentoOneHistogram(models.Model):
    datamov = models.DateField()
    importo = models.IntegerField()
    email = models.TextField()
    class Meta:
        managed = False
        db_table = 'greetings_movimentoonehistogram'

class MovimentoOneLine(models.Model):
    datamov = models.DateField()
    importo = models.IntegerField()
    email = models.TextField()
    class Meta:
        managed = False
        db_table = 'greetings_movimentooneline'


