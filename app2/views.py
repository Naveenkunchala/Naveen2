from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Anil(request):
    return HttpResponse('<h1>Best left hand batsman</h1>')


def Harikarishna(request):
    return HttpResponse('<h1>Best Bower in my college</h1>')

