# entry/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'entry/index.html')


def ky_0141_1(request):
    return render(request, 'entry/KY-0141.html')
