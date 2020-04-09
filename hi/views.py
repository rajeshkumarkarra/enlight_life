from django.shortcuts import render, redirect
#from django.template import Context
from django.contrib.auth.models import User, auth
from django.utils.datastructures import MultiValueDictKeyError
#from .import views


# Create your views here.
def home(request):
    
    return render(request, 'home.html', {'name': 'Rajeshkumar'})


   
    
def add(request):
    #template = 'home.html'
    #try:
    if request.method == 'POST':
        if 'number1' in request.POST:
            val1 = request.GET['number1']
        else:
            number1 = False
        val2 = request.GET['number2']
        res = val1 + val2
        return redirect('/')
    else:
        return render(request, 'hi/result.html', {'result': res})
    #except MultiValueDictKeyError:
        #raise AttributeError('MultiValueDictKeyError') 
