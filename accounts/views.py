from django.shortcuts import render, redirect
#from .import views
from django.contrib.auth.models import User, auth
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            
            username = request.POST['username']
        else:
            username = False
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        if 'fist_name' in request.POST:
            first_name = request.POST['fist_name']
        else:
            first_name=False
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists(): 
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1,  email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            
            messages.info(request, 'Password not matching!!')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
        