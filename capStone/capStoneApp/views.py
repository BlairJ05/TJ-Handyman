from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'index.html')


def signUp(request):
    return render(request, 'signUp.html')

def signIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'signIn.html', {'form': form})

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('signIn')
    else:
        form = UserCreationForm()
    return render(request, 'signUp.html', {'form': form})


def signOut(request):
    logout(request)
    return redirect('index')


def Assembly(request):
    return render(request, 'Assembly.html')

def Carpenter(request):
    return render(request, 'Carpenter.html')

def Home_Repairs(request):
    return render(request, 'Home_Repairs.html')

def Instulation(request):
    return render(request, 'Instulation.html')

def More_About_Me(request):
    return render(request, 'More_About_Me.html')

def Moving(request):
    return render(request, 'Moving.html')

def Outdoor_Help(request):
    return render(request, 'Outdoor_Help.html')

def Painting(request):
    return render(request, 'Painting.html')