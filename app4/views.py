from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vaseem(request):
    return HttpResponse('<h1><marquee> vaseem is a very worst boy</marquee></h1>')
