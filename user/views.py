from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to QA Office.<br/>"
                        "This is the page to manage users.<br />"
                        "Empty Now.")
