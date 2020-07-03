# entry/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ky0141/', views.ky_0141_1, name="ky_0141")
]
