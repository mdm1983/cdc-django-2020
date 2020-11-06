# greetings/views.py
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from . serializers import GreetingSerializer
from . models import Greeting

from django.utils.timezone import now
from django.db import models
from django.db import connection

from django.utils import timezone

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the greetings index 4.")


class greetingsList(APIView):

    template = 'index.html';
    def get(self,request):
        greetings1 = Greeting.objects.all()
        #return HttpResponse(greetings1[0].name)
        serializer = GreetingSerializer(greetings1, many=True)
        #return Response(serializer.data)
        return render(request, self.template, {'greetings': serializer.data})

class insert(APIView):
    def __maxId(self):
        cursor = connection.cursor()
        cursor.execute('SELECT max(id)+1 as max_id FROM greetings_greeting')
        return cursor.fetchone()[0]

    def get(self, request):
        sysdate = timezone.now()
        sysdateString = str(sysdate.day) + "_" + str(sysdate.month) + "_" + str(sysdate.year)
        greeting = Greeting()
        greeting.id = self.__maxId()
        greeting.name = request.GET.get('name', "name" + sysdateString)
        greeting.surname = request.GET.get('surname', "surname" + sysdateString)
        greeting.save()
        return HttpResponse(greeting.name + " " + greeting.surname)
