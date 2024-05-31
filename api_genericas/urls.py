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
    AutorDbViewSet,
)
router = DefaultRouter()
router.register('autores',AutorDbViewSet,basename='autores')
urlpatterns = [
    path('autores-list/',AutorDbAPIList.as_view(),name='autores_List'),
    path('autores-create/',AutorDbAPICreate.as_view(),name='autores_create'),
    path('autores-retrieve/<int:pk>',AutorDbAPIRetrieve.as_view(),name='autores_retrieve'),
    path('autores-delete/<int:pk>',AutorDbAPIDelete.as_view(),name='autores_delete'),
    path('libros-list/',LibroDbAPIList.as_view(),name='libros_list'),
    path('libros-create/',LibroDbAPICreate.as_view(),name='libros_create'),
    path('libros-retrieve/<int:pk>',LibroDbAPIRetrieve.as_view(),name='libros_retrieve'),
    path('libros-delete/<int:pk>',LibroDbAPIDelete.as_view(),name='libros_delete'),
]
urlpatterns +=router.urls