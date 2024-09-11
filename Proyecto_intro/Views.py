from django.http import HttpResponse

def introduccion(request):
    return HttpResponse("hola")