from django.urls import  path
from django.views import View

from mundial_api import views
import mundial_api
#radio_api.urls

urlpatterns = [
    #path('jugadores/', views.verEquipo),
    path('jugador/editar/', views.EditarJugador),



]


