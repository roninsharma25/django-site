from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'studentPortal.html')

def index(request):
    return HttpResponse("Hello, world. You're at the portal index.")
