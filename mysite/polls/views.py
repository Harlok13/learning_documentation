# Здесь находятся сами представления
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('hello, world. You\'re at the polls index')
