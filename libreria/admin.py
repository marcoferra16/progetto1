from django.contrib import admin
from .models import GENERE_fm, AUTORE_fm, LIBRO_fm
# Register your models here.

admin.site.register(GENERE_fm)
admin.site.register(AUTORE_fm)
admin.site.register(LIBRO_fm)