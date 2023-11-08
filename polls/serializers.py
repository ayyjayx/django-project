from rest_framework import serializers
from .models import Stanowisko, Plec, Osoba

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
        fields = ['imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']
        read_only_fields = ['data_dodania']
        
