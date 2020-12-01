# greetings/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from . serializers import MovimentoOneSerializer, MovimentoHistogramSerializer, MovimentoLineSerializer
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

from datetime import datetime
import datetime as datetimealias
from random import randrange
from datetime import timedelta
from random import seed
from random import randint

from . models import MovimentoOne, MovimentoHistogramOne, MovimentoLineOne

import pytz

from .producer import producer

from kafka import TopicPartition

from time import sleep

import json

from django.forms.models import model_to_dict

# Create your views here.
def index(request):

    KAFKA_TOPIC = 'Topic5'

    # To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer (KAFKA_TOPIC,bootstrap_servers = ['10.7.192.64:9092'], api_version=(0, 10, 1),
    auto_offset_reset='earliest', 
    #group_id='myTestGroupId', 
    consumer_timeout_ms=3000)
    #ip dinamico della macchina di dario

    consumer.subscribe(KAFKA_TOPIC)

    producer.main()

    outputString = ''
    for message in consumer:
        outputString = outputString + message.value.decode("utf-8")
        outputString = outputString + ";"

    return HttpResponse(outputString)
    #return HttpResponse("Hello, world. You're at the greetings index 4.")

class greetingsList(APIView):

    template = 'index.html';
    def get(self,request):
        cursor = connection.cursor()
        recordsMovimento = MovimentoOne.objects.all().filter(email=request.user.username)
        serializer = MovimentoOneSerializer(recordsMovimento, many=True)
        recordsMovimentoHistogram = MovimentoHistogramOne.objects.all().filter(email=request.user.username)
        serializerHistogram = MovimentoHistogramSerializer(recordsMovimentoHistogram, many=True)
        recordsMovimentoLine = MovimentoLineOne.objects.all().filter(email=request.user.username)
        serializerLine = MovimentoLineSerializer(recordsMovimentoLine, many=True)
        return render(request, self.template, {'greetings_movimentoone': serializer.data, 'loggedas': request.user.username, 'greetings_movimentohistogram': serializerHistogram.data, 'greetings_movimentoline': serializerLine.data })

class insert(APIView):
    def __maxId(self):
        cursor = connection.cursor()
        cursor.execute('SELECT max(id)+1 as max_id FROM greetings_movimentoone')
        return cursor.fetchone()[0]

    def __random_date(self, start, end):
        """
        This function will return a random datetime between two datetime 
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    def __myconverter(self, o):
        if isinstance(o, datetimealias.datetime):
            print('datetime ' + o)
            return o.isoformat()
        #elif isinstance(o, date):
            #return o.isoformat()

    def get(self, request):

        email = request.GET.get('email', "")

        topic = email.replace("@", "")

        # To consume latest messages and auto-commit offsets
        consumer = KafkaConsumer (topic,bootstrap_servers = ['10.7.192.64:9092'], api_version=(0, 10, 1),
        auto_offset_reset='earliest', 
        #group_id='myTestGroupId', 
        consumer_timeout_ms=3000)
        #ip dinamico della macchina di dario

        consumer.subscribe(topic)

        d1 = datetime.strptime('1/1/2020 GMT', '%m/%d/%Y %Z')
        d2 = datetime.strptime('12/31/2020 GMT', '%m/%d/%Y %Z')
        
        sysdate = timezone.now()
        sysdateString = str(sysdate.day) + "." + str(sysdate.month) + "." + str(sysdate.year)
        negativo = False
        producer = KafkaProducer(bootstrap_servers=['10.7.192.64:9092'], api_version=(0, 10, 1))

        for _ in range(50):
            movimento = MovimentoOne()
            movimento.id= self.__maxId()
            movimento.datamov = self.__random_date(d1, d2)
            movimento.datamov =  movimento.datamov.replace(tzinfo=timezone.utc)
            movimento.email = email
            if (negativo):
                movimento.importo = randint(-50, -1)
                negativo = False
            else:
                movimento.importo = randint(1, 100)
                negativo = True
            movimento.causale = "auto generated " + sysdateString
            
            jsonStr = json.dumps({'id' : movimento.id, 
                'datamov': str(movimento.datamov.day) + "-" + str(movimento.datamov.month) + "-" + str(movimento.datamov.year), 
                'email': movimento.email, 
                'importo': movimento.importo, 
                'causale': movimento.causale})
            producer.send(topic, jsonStr.encode('utf-8'))
            movimento.save()

        #i=0
        #for message in consumer:
            #print(str(i) + " " + message.value.decode("utf-8"))
            #i=i+1
        
        return HttpResponseRedirect('/greetings/getList')





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
