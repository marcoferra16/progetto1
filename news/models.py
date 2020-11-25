from django.db import models

class Giornalista(models.Model):
    nome= models.CharField(max_length=20)
    cognome= models.CharField(max_length=20)

    def __str__(self):
       return self.nome + " " + self.cognome
    
    class Meta:
        verbose_name='giornalista'
        verbose_name_plural='giornalisti'

class Articolo (models.Model):
    titolo= models.CharField(max_length=100)
    contenuto= models.TextField()
    giornalista= models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name='articolo'
        verbose_name_plural='articoli'