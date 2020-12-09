from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import AUTORE_fm, LIBRO_fm, 
# Create your views here.

class AutoreDetail_fm(DetailView):
    model = AUTORE_fm
    template_name = "autore.html"

class LibroList_fm(ListView):
    model = LIBRO_fm
    template_name = "libro.html"



