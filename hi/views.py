from django.shortcuts import render
#from django.template import Context


# Create your views here.
def home(request):
    
    return render(request, 'home.html', {'name': 'Rajeshkumar'})


   
    
def add(request):
    #template = 'home.html'
    #try:
    val1 = int(request.GET["number1"])
    val2 = int(request.GET["number2"])
    res = val1 + val2
    return render(request, 'result.html', {'result': res})
    #except MultiValueDictKeyError:
        #raise AttributeError('MultiValueDictKeyError') 
