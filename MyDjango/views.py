from django.shortcuts import render
from django.http import HttpResponse
from MyDjango import tests as testdb


# Create your views here.
def index(request):
    msg = testdb.db_read()
    return HttpResponse('Hello World ! This is from MyDjango Project...<p>' + msg + '</p>')