from rest_framework import serializers
from .models import Stanowisko, Osoba
from django.contrib.auth.models import User
import datetime

class StanowiskoSerializer(serializers.Serializer):
    nazwa = serializers.CharField(required=True)
    opis = serializers.CharField(required=False, allow_blank=True)
    
    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance
    
class OsobaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania', 'wlasciciel']
        read_only_fields = ['data_dodania', 'wlasciciel']
        wlasciciel = serializers.ReadOnlyField(source='User.username')
        
    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Imie ma zawierac tylko litery.")
        return value

    def validate_data_dodania(self, value):
        if value > datetime.now():
            raise serializers.ValidationError("Data nie moze byc z przyszlosci.")
        return value
    
    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.data_dodanie = validated_data.get('data_dodania', instance.data_dodania)
        instance.save()
        return instance