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

class MovimentoHistogramOne(models.Model):
    datamov = models.DateField()
    importo = models.IntegerField()
    email = models.TextField()
    class Meta:
        managed = False
        db_table = 'greetings_movimentohistogramone'

class MovimentoLineOne(models.Model):
    datamov = models.DateField()
    importo = models.IntegerField()
    email = models.TextField()
    class Meta:
        managed = False
        db_table = 'greetings_movimentolineone'


