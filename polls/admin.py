from django.contrib import admin
from .models import Osoba, Stanowisko
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ["nazwa"]

@admin.display(description="Name")
def stanowisko_i_id(obj):
    return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ["data_dodania"]
    list_display = ["imie", "nazwisko", stanowisko_i_id]
    list_filter = ("stanowisko", "data_dodania")
    
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)
