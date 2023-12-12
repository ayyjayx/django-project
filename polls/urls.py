from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoba/', views.osoba_list_all.as_view()),
    path('osoba/<int:pk>/', views.osoba.as_view()),
    path('osoba/<str:string>/', views.osoba_contains_strings.as_view()),
    path('stanowisko/', views.stanowisko_list_all),
    path('stanowisko/<int:pk>/', views.stanowisko),
]