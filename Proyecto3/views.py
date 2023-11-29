from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Pagina web- Ram")