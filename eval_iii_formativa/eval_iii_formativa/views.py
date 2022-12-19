from django.contrib.auth import authenticate,logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework.response import Response



#token "token": "ade6617cab403bed8816c5b011223e25e24407ca"
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login (request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response ({'error': 'Por favor ingrese Uruario y/o Contraseña'},
        status = status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username,password=password)


    if not user:
        return Response ({'error':'Credencial no válidas'},
                        status= status.HTTP_404_NOT_FOUND)
        
    token, _ = Token.objects.get_or_create(user=user)
    return Response ( {'token': token.key},
                    status=status.HTTP_200_OK)



@api_view (['POST','GET'])
@permission_classes([IsAuthenticated])
def UserLogout(request):
    request.user.auth_token.delete()#borrar token de usuario
    logout(request)#cerrar sesion del usuario que hizo request
    return Response({'status':'Se ha Cerrado sesion exitosamente'},
                    status=status.HTTP_200_OK)