from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AutorDbAPIList,
    AutorDbAPICreate,
    AutorDbAPIRetrieve,
    AutorDbAPIDelete,
    LibroDbAPIList,
    LibroDbAPICreate,
    LibroDbAPIRetrieve,
    LibroDbAPIDelete,
    AutorLibrosDbAPIList,
    AutorDbViewSet,
    ExampleListCreate
    
)
router = DefaultRouter()#definir un router
router.register('autores',AutorDbViewSet,basename='autores')# registra cual es el camino a seguir
urlpatterns = [
    path('autores-list/',AutorDbAPIList.as_view(),name='autores_List'),
    path('autores-libros/',AutorLibrosDbAPIList.as_view(),name='autores_libros'),
    path('autores-create/',AutorDbAPICreate.as_view(),name='autores_create'),
    path('autores-retrieve/<int:pk>',AutorDbAPIRetrieve.as_view(),name='autores_retrieve'),
    path('autores-delete/<int:pk>',AutorDbAPIDelete.as_view(),name='autores_delete'),
    path('libros-list/',LibroDbAPIList.as_view(),name='libros_list'),
    path('libros-create/',LibroDbAPICreate.as_view(),name='libros_create'),
    path('libros-retrieve/<int:pk>',LibroDbAPIRetrieve.as_view(),name='libros_retrieve'),
    path('libros-delete/<int:pk>',LibroDbAPIDelete.as_view(),name='libros_delete'),
    path('examples/', ExampleListCreate.as_view(), name='example-list'),
]
urlpatterns +=router.urls