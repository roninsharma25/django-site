from django.http import HttpResponse
from django.shortcuts import render
from . import models

def home(request):
    return render(request, 'studentPortal.html')

def test(request):
    name = request.GET.get('name')
    if name is not None:
        command = 'SELECT * from studentportalapp_student WHERE studentName = ' + f'"{name}"'
        names = []
        results = models.Student.objects.raw(command)
        if len(results) > 0:
            for s in results:
                names.append(s.studentName)
            return HttpResponse(names)
        else:
            return HttpResponse("No students with that name!")
    else:
        return HttpResponse("Invalid Name!")

def index(request):
    return HttpResponse("Hello, world. You're at the portal index.")
