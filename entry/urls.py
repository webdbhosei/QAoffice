# entry/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ky0141/', views.ky_0141_1, name="ky_0141"),
    path('ry0011/', views.ry_0011_1, name="ry_0011"),
    path('ry0011/RY-pdf/', views.ry_0011_2, name="ry_0011_2")
]
