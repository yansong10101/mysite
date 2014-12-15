__author__ = 'yansong'
from django.conf.urls import url
from MyDjango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]