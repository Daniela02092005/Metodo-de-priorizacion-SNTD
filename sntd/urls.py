from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registrar/", views.registrar, name="registrar"),
    path("listar/", views.listar, name="listar"),
    path("completar/<int:id>/", views.completar, name="completar"),
    path("eliminar/<int:id>/", views.eliminar, name="eliminar"),
]
