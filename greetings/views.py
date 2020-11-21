# greetings/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from . serializers import GreetingSerializer
from . models import Greeting

from django.utils.timezone import now
from django.db import models
from django.db import connection

from django.utils import timezone

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Import KafkaProducer from Kafka library
from kafka import KafkaProducer

# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer

# Import JSON module to serialize data
import json

# Create your views here.
def index(request):

    # Initialize producer variable and set parameter for JSON encode
    producer = KafkaProducer(bootstrap_servers =
    ['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    # Send data in JSON format
    producer.send('JSONtopic', {'name': 'fahmida','email':'fahmida@gmail.com'})
    
    # Print message
    print("Message Sent to JSONtopic")

    # Initialize consumer variable and set property for JSON decode
    consumer = KafkaConsumer ('JSONtopic',bootstrap_servers = ['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    outputString = ""
    # Read data from kafka
    for message in consumer:
        outputString = outputString + "\nConsumer records:\n"
        outputString = outputString + message
        outputString = outputString + "\nReading from JSON data\n"
        outputString = outputString + "Name:" + message[6]['name']
        outputString = outputString + "Email:" + message[6]['email']

    return HttpResponse(outputString)
    #return HttpResponse("Hello, world. You're at the greetings index 4.")

class greetingsList(APIView):

    template = 'index.html';
    def get(self,request):
        greetings1 = Greeting.objects.all()
        serializer = GreetingSerializer(greetings1, many=True)
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





class Login(APIView):
    template = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/greetings/getList')
        else:
            return render(request, self.template, {'form': form})




class Register(APIView):
    template = 'register.html'

    def get(self, request):
        return render(request, self.template)


    def post(self, request):
        form = AuthenticationForm(request.POST)
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        user.last_name = request.POST['lastName']
        user.first_name = request.POST['firstName']

        if request.POST['password'] != request.POST['confirmPassword']:
            return render(request, self.template, {'form': form})
        else:
            user.save()
            return HttpResponseRedirect('/greetings/login')
