from django.http import HttpResponse
from django.shortcuts import render
def introduccion(request):
    return HttpResponse("hola")

def welcome(request):
    return render(request,'TestTrivia/Trivia.html')