from django.urls import path
from .views import LibroList_fm, AutoreDetail_fm
app_name='libreria'
urlpatterns = [
    path('',LibroList_fm.as_view(), name="lista_libri"),
    path('autore/<int:pk>/',AutoreDetail_fm.as_view(), name="profilo_autore")    
]