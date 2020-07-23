# entry/views.py
from django.shortcuts import render
#from django.http import FileResponse
from django.http import HttpResponse


def index(request):
    return render(request, 'entry/index.html')


def ky_0141_1(request):
    return render(request, 'entry/KY-0141.html')

def ky_0141_2(request):
    return render(request, 'entry/KY/KY_0141.html')

def ky_0141_css(request):
    response = HttpResponse(open('templates/entry/KY/KY_0141.css', 'r').read(), content_type='text/css')
    return response

def ky_0141_js(request):
    response = HttpResponse(open('templates/entry/KY/KY_0141.js', encoding='utf-8',mode='r').read(), content_type='text/javascript')
    return response

def ky_0141_pdf(request):
    response = HttpResponse(open('templates/entry/KY/Object Oriented Web Programming Question input page.pdf', 'rb').read(), content_type='application/pdf')
    return response

def ry_0011_1(request):
    return render(request, 'entry/RY-0011.html')

def ry_0011_2(request):
    response = HttpResponse(open('templates/entry/RY-pdf/Object_web_auth.pdf', 'rb').read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Object_web_auth.pdf"'
    return response

def yh_0010_1(request):
    return render(request, 'entry/YH-0010.html')

def yh_0010_2(request):
    response = HttpResponse(open('templates/entry/YH-pdf/20t0010_admin.pdf', 'rb').read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="20t0010_admin.pdf"'
    return response