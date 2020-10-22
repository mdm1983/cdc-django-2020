# greetings/views.py
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from . serializers import GreetingSerializer
from . models import Greeting
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the greetings index 4.")


class greetingsList(APIView):
    def get(self,request):
        greetings1 = Greeting.objects.all()
        #return HttpResponse(greetings1[0].name)
        serializer = GreetingSerializer(greetings1, many=True)
        return Response(serializer.data)