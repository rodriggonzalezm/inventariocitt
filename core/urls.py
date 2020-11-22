from django.urls import path
from .views import inicio, login, registrar, comomedir, comprar, contactanos, encuentranos, listadocortinas, nuevacortina, modificarcortina, eliminarcortinas, registrousuario

urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('registrar/', registrar, name="registrar"),
    path('comomedir/', comomedir, name="comomedir"),
    path('comprar/', comprar, name="comprar"),
    path('contactanos/', contactanos, name="contactanos"),
    path('encuentranos/', encuentranos, name="encuentranos"),
    path('listadocortinas/', listadocortinas, name="listadocortinas"),
    path('nuevacortina/', nuevacortina, name="nuevacortina"),
    path('modificarcortina/<id>/', modificarcortina , name="modificarcortina"),
    path('eliminarcortinas/<id>/', eliminarcortinas , name="eliminarcortinas"),
    path('registro/', registrousuario , name="registrousuario"),
]