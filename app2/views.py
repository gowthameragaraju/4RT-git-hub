from django.shortcuts import render

# Create your views here.
def poorna(request):
    d={'loc':'Nellore','code':'My Bactch Code Is 74YM1'}
    return render(request,'jinjaprint1.html',d)