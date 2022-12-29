from django.urls import path
from app1.views import *
app_name='somthing!'
urlpatterns=[
    path("gowtham/",gowtham,name='gowtham'),
]