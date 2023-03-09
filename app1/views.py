from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dhoni(request):
    return HttpResponse('<h1>The Good Finisher In The World</h1>')



def Naveen(request):
    return HttpResponse('<h1>The best Hitter</h1>')
