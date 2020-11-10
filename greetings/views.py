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

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the greetings index 4.")

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
