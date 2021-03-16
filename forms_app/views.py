from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse

# Create your views here.
def contatti(request):

    #se la richiesta è d tipo POST, allora possiamo processare i dati
    if request.method == "POST":

        #creiamo l'istanza del form e la popoliamo con i dati della POST request (processo di "binding")
        form = FormContatto(request.POST)

        #is_valid() controlla se il form inserito è valido:
        if form.is_valid():
         # a questo punto possiamo usare i dati validi!
         # tenere a mente che cleaned_data["nome_dato"] ci permette di accedere ai dati validi e convertiti in tipi standard di Python
         print("Il Form è valido!")
         print("NOME: ",form.cleaned_data["nome"])
         print("COGNOME: ",form.cleaned_data["cognome"])
         print("EMAIL: ",form.cleaned_data["email"])
         print("CONTENUTO: ",form.cleaned_data["contenuto"])
         
         #ringrazio l'utente per averci contattato - volendo possiamo effettuare un redirect a una pagina specifica
         return HttpResponse("<h1>Grazie per averci contattato!</h1>")

    #se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo, allora creo il form di default vuoto
    else:
        form = FormContatto()

    #arriviamo a questo punto se si tratta della prima volta che la pagina viene richiesta (con metodo GET), o se il form non è valido e ha errori
    context = {"form": form}
    return render(request, "contatto.html", context)