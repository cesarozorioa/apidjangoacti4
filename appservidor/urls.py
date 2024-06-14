from django.urls import path
from .views import getMensaje,autorView,AutorAPIjson,AutorAPIxml
urlpatterns = [
    path('',getMensaje, name='getMensaje'),
    path('autor/<int:id>',autorView,name='autorView'),
    path('api/lista-autores-json/',AutorAPIjson,name='autor_json'),
    path('api/lista-autores-xml/',AutorAPIxml,name='autor_xml')
]