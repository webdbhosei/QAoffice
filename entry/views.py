# entry/views.py
from django.shortcuts import render
#from django.http import FileResponse
from django.http import HttpResponse


def index(request):
    return render(request, 'entry/index.html')


def ky_0141_1(request):
    return render(request, 'entry/KY-0141.html')

def ry_0011_1(request):
    return render(request, 'entry/RY-0011.html')

def ry_0011_2(request):
    response = HttpResponse(open('templates/entry/RY-pdf/Object_web_auth.pdf', 'rb').read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Object_web_auth.pdf"'
    return response

