from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout


def Request(request):
    return render(request, 'request_a_project.html')

def gallery(request):
    return render(request, 'gallery.html')

def index(request):
    return render(request, 'index.html')

def pricing(request):
    return render(request, 'pricing.html')

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
                return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signUp.html', {'form': form})

def signIn(request):
    password_error = False

    if request.method == 'POST':
        if 'signin' in request.POST:
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
        elif 'signup' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                    password_error = True
                else:
                    form.save()
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password1')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('index')

    form_signin = AuthenticationForm()
    form_signup = UserCreationForm()
    return render(request, 'signIn.html', {'form_signin': form_signin, 'form_signup': form_signup, 'password_error': password_error})

def signOut(request):
    logout(request)
    return redirect('index')

def Assembly(request):
    return render(request, 'Assembly.html')

def Carpenter(request):
    return render(request, 'Carpenter.html')

def Home_Repairs(request):
    return render(request, 'Home_Repairs.html')

def Installation(request):
    return render(request, 'Instulation.html')

def More_About_Me(request):
    return render(request, 'More_About_Me.html')

def Moving(request):
    return render(request, 'Moving.html')

def Outdoor_Help(request):
    return render(request, 'Outdoor_Help.html')

def Painting(request):
    return render(request, 'Painting.html')


@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user 
            review.save()
            return redirect('index') 
        else:
            pass
    else:
        form = ReviewForm()

    return render(request, 'submit_review.html', {'form': form})


@login_required
def reviews(request):
    reviews = Review.objects.all() 
    return render(request, 'reviews.html', {'reviews': reviews})
