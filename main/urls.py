from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.NewProfileView, name="form"),
    path('mail', views.index, name="mail")
]