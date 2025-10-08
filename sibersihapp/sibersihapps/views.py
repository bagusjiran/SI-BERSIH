from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Halo, Dunia! Ini adalah halaman blog pertama saya wazzah.</h1>")


# Create your views here.
