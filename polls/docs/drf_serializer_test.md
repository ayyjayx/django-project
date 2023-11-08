from polls.models import Osoba, Stanowisko
from polls.serializers import StanowiskoSerializer, OsobaModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

stanowisko = Stanowisko(nazwa='kasjer', opis='')
stanowisko.save()
serializer = StanowiskoSerializer(stanowisko)
serializer.data
content = JSONRenderer().render(serializer.data)
content
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = StanowiskoSerializer(data=data)
deserializer.is_valid()
deserializer.fields
deserializer.validated_data
deserializer.save()
deserializer.data

osoba = Osoba(imie='Konrad', nazwisko='Budyn', plec=1, stanowisko=stanowisko)
osoba.save()
serializer = OsobaModelSerializer(osoba)
serializer.data
content = JSONRenderer().render(serializer.data)
content
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = OsobaModelSerializer(data=data)
deserializer.is_valid()
deserializer.fields
deserializer.validated_data
deserializer.save()
deserializer.data