from rest_framework import serializers
from appservidor.models import AutorDb,LibroDb
from .models import Example

class AutorDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorDb
        fields = '__all__'

class AutorLibrosSerializer(serializers.ModelSerializer):
    libros = serializers.StringRelatedField(many=True)
    class Meta:
        model = AutorDb
        fields = '__all__'
        #fields = ('id','nombre','email','libros')
        

class LibroDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroDb
        fields = '__all__'

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = '__all__'