from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoba/', views.osoba_list_all),
    path('osoba/<int:pk>/', views.osoba),
    path('osoba/delete/<int:pk>/', views.osoba_delete),
    path('osoba/create/', views.osoba_create),
    path('osoba/<str:string>/', views.osoba_contains_string),
    path('stanowisko/', views.stanowisko_list_all),
    path('stanowisko/<int:pk>/', views.stanowisko),
    path('login/', include('rest_framework.urls'))
]