from django.shortcuts import render
from django.http import HttpResponse
from AppAle import peliculas



def peliculas(request):
    lista = Pelicula.objects.all()
    return render(request, "peliculas.html", {"peliculas": lista})

 def musica(request):
    lista = Musica.objects.all()
    return render(request, "musica.html", {"musica": lista})

def auto(request):
    lista = Auto.objects.all()
    return render(request, template_name="hobby.html") context:{"Auto": lista})



