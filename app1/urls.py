from app1.views import *

from django.urls import path

app_name='somthing'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('Naveen/',Naveen,name='Naveen'),
]