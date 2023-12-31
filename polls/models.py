from django.db import models
from django.contrib.auth.models import User


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60)
    opis = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return f"{self.nazwa}"
    class Meta:
        permissions = [
            ("can_view_other_positions", "Pozwala na spojrzenie na inne stanowiska")
        ]

class Plec(models.IntegerChoices):
    MEZCZYZNA = 1
    KOBIETA = 2
    INNE = 3
    
class Osoba(models.Model):
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    plec = models.IntegerField(choices=Plec.choices)
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateField(auto_now_add=True)
    wlasciciel = models.ForeignKey(User, related_name='Osoba', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
    
    class Meta:
        ordering = ["nazwisko"]
        permissions = [
            ("can_view_other_persons", "Pozwala na spojrzenie na inne osoby")
        ]
