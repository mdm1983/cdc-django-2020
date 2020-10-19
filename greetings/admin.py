from django.contrib import admin

# Register your models here.

from greetings.models import Greeting

admin.site.register(Greeting)