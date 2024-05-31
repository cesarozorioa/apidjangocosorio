from rest_framework import serializers
from appservidor.models import AutorDb,LibroDb

class AutorDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorDb
        fields = '__all__'

class LibroDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroDb
        fields = '__all__'