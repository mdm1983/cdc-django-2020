from rest_framework import serializers
from .models import Greeting
from .models import MovimentoOne


class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        #        fields = ('name', 'surname', 'greeting')
        fields = '__all__'

class MovimentoOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentoOne
        fields = ('datamov', 'causale', 'importo', 'email')
        #fields = '__all__'
