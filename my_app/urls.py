
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("index_html", views.index_html, name="index_html"),
    path("acerca_de", views.acerca_de, name="acerca_de"),
    path("cursos", views.cursos, name="cursos"),
    path("cursos_json", views.cursos_json, name="cursos_json"),
    path("cotizacion_dollar", views.cotizacion_dollar, name="cotizacion_dollar"),
    path("aeropuertos", views.aeropuertos, name="aeropuertos"),
    path("aeropuertos_json", views.aeropuertos_json, name="aeropuertos_json")
]
