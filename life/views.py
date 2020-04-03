
"""
from django.shortcuts import render
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'life/index.html')

def portfolio(request):
    return render(request, 'life/portfolio.html')

def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')
        
        c = Contact(email=email_r, subject = subject_r, message = message_r)
        c.save()
        
        
        return render(request, 'life/thank.html')
    else:
        return render(request, 'life/contact.html')
        
"""

# views.py is responsiable to display the stuff on web browser

"""
# Create your views here.
# HttpResponse is responsiable for displaying the stuff on web browser
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello rajesh! welcome to the tech world")
"""
# request is basically user sends a request to server
# render is working on index.html file and hide waste stuff and render some results to user
from django.shortcuts import render
from .models import Contact
import requests, json
def index(request):
    if request.method == 'POST':
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        
        r =requests.get('http://api.icndb.com/jokes/random?firstName'+ firstname + '&lastName=' +lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joker': joke}
        return render(request, 'life/index.html', context)
    else:
        
        firstname='rajeshkumar'
        lastname='kumar'
        
        r =requests.get('http://api.icndb.com/jokes/random?firstName'+ firstname + '&lastName=' +lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joker': joke}
        return render(request, 'life/index.html', context)

def downloads(request):
    return render(request, 'life/downloads.html')

def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')
        
        c = Contact(email=email_r, subject = subject_r, message = message_r)
        c.save()
        return render(request, 'life/thank.html')
    else:
        return render(request, 'life/contact.html')
    
    # c = Student(first_name ='', last_name='')

