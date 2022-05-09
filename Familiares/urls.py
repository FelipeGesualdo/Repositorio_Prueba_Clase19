from django.urls import path
from .views import mostrar_Familiares

urlpatterns = [
    path('/', mostrar_Familiares),
    path('/crear',crear_Familiar, nombre='crear_Familiar')
    path('/eliminar/<id>',borrar_Familiar, nombre='borrar_Familiar')
]