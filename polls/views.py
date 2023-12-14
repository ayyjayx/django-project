from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoSerializer


class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"
    
def index(request):
    return HttpResponse("Hello World. You are at the poll index.")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@permission_required('polls.view_stanowisko')
def stanowisko_list_all(request):
    if request.method == 'GET':
        stanowiska_list = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska_list, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def stanowisko(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        stanowisko = Stanowisko.objects.get(pk=pk)
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StanowiskoSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'POST':
        serializer = StanowiskoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_list_all(request):
    if request.method == 'GET':
        osoby = Osoba.objects.all()
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def osoba(request, pk):
    # if not request.user.has_perm('polls.view_osoba'):
    if not request.user.has_perm('polls.can_view_other_persons'):
        raise PermissionDenied()
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = OsobaModelSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_delete(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def osoba_create(request):
    if request.method == 'POST':
        serializer = OsobaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def osoba_contains_string(request, string):
    if request.method == 'GET':
        osoba = Osoba.objects.filter(nazwisko__contains=string)
        serializer = OsobaModelSerializer(osoba, many=True)
        return Response(serializer.data)