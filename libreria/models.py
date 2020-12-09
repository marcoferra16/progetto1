from django.db import models

# Create your models here.
class GENERE_fm(models.Model):
    nome= models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

class AUTORE_fm(models.Model):
    nome= models.CharField(max_length=20)
    cognome= models.CharField(max_length=20)
    nazione= models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"

class LIBRO_fm(models.Model):
    titolo= models.CharField(max_length=100)
    isbn= models.CharField(max_length=13)
    autore= models.ForeignKey(AUTORE_fm, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(GENERE_fm)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"
    
