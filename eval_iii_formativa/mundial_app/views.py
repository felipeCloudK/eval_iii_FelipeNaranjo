
# Create your views here.
from django.shortcuts import render
from mundial_api.models import Jugador
from mundial_api.models import Equipo
from django.contrib.auth import authenticate, logout
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from mundial_api.serializers import EquipoSerializer,JugadorSerializer
from mundial_api import serializers
from rest_framework.authtoken.models import Token

@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def verEquipo(request):
    equipo = Equipo.objects.all()
    data = {'equipo': equipo}
    return render(request,'Equipos/Equipo.html',data)


@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def IdEquipo(request, id):
    equipoc = Equipo.objects.filter(id=id).first()
    data = {'equipo': equipoc}
    return render(request,'Equipos/Idequipo.html',data)
        
#def verEquipo(request):
    equipo = Equipo.objects.all()
    data = {'equipo': equipo}
    return render(request, 'layout.html',data)