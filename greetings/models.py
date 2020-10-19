from django.db import models

# Create your models here.

class Greeting(models.Model):

    name = models.TextField()
    surname = models.TextField()

    greeting = models.TextField()