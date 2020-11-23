from rest_framework import serializers
from .models import Greeting
from .models import MovimentoOne, MovimentoHistogramOne, MovimentoLineOne


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

class MovimentoHistogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentoHistogramOne
        fields = ('datamov', 'importo', 'email')
        #fields = '__all__'

class MovimentoLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentoLineOne
        fields = ('datamov', 'importo', 'email')
        #fields = '__all__'
