from django.urls import path

from mundial_app import views


urlpatterns = [
    path('equipos/', views.verEquipo),
    path('equipo/<int:id>', views.IdEquipo),
    path('jugador/editar/<int:id>', views.gestionarJugador)
]