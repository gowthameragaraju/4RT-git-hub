from django.shortcuts import render

# Create your views here.
def gowtham(request):
    d={'name':'DJANGO'}
    return render(request,'jinja_print.html',d)