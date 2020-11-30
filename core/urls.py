from django.urls import path, include
from .views import inicio, login, comomedir, comprar, contactanos, encuentranos, listadocortinas, nuevacortina, modificarcortina, eliminarcortinas, registrousuario, CortinasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cortinas', CortinasViewSet)

urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('comomedir/', comomedir, name="comomedir"),
    path('comprar/', comprar, name="comprar"),
    path('contactanos/', contactanos, name="contactanos"),
    path('encuentranos/', encuentranos, name="encuentranos"),
    path('listadocortinas/', listadocortinas, name="listadocortinas"),
    path('nuevacortina/', nuevacortina, name="nuevacortina"),
    path('modificarcortina/<id>/', modificarcortina , name="modificarcortina"),
    path('eliminarcortinas/<id>/', eliminarcortinas , name="eliminarcortinas"),
    path('registrousuario/', registrousuario , name="registrousuario"),
    path('api/', include(router.urls)),
]