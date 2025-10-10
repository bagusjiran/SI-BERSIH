from django.shortcuts import render
from django.http import HttpResponse

def landingpage(request):
    return render(request, 'web/index.html')

def adminpage(request):
    return render(request, 'administrator/index.html')



# Create your views here.
