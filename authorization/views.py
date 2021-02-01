from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            credentials = User.objects.get(email = email)
            if (credentials.password == password):
                request.session['email'] = email
                return redirect('index')
            else:
                return render(request, 'login.html', {'error': 'invalid'})
        except User.DoesNotExist:
            #report error
            return render(request, 'login.html', {'error':'invalid'})

    return render(request, 'login.html', {})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User
        try:
            obj = user.objects.create(name=name, email=email, password= password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'register.html', {})

    return render(request, 'register.html', {})

def logout(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]
    return redirect('index')
