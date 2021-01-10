from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^books/$', views.book_list, name="list"),
    url(r'^books/(?P<pk>[0-9]+)$', views.books_detail, name="detail")
   
]