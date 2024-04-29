from itertools import groupby
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from .models import Review
from .decorators import *
from django.contrib.auth.decorators import *
from django.contrib import messages
import openai
from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Chat
from django.http import JsonResponse
from django.contrib import messages
from openai import OpenAI
from django.utils import timezone
from django.http import JsonResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponseRedirect
from .forms import InvoiceForm


client = OpenAI(api_key="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")


def more_user(request, user_id=None, username=None):
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    elif username:
        user = get_object_or_404(User, username=username)
    else:
        return HttpResponseBadRequest("Invalid request")

    users = User.objects.all()

    reviews = user.reviews.all()

    return render(
        request,
        "admin_page.html",
        {"users": users, "selected_user": user, "reviews": reviews},
    )


def submit_form(request):
    if request.method == "POST":
        form_data = request.POST
        file_data = request.FILES.get("filename", None)
        request_model = RequestModel(
            name=form_data["name"],
            number=form_data["number"],
            email=form_data["email"],
            location=form_data["location"],
            date=form_data["date"],
            message=form_data["message"],
            filename=file_data,
        )
        request_model.save()
    return render(request, "request_a_project.html")


def user_list(request):
    users = User.objects.all()
    return render(request, "admin_page.html", {"users": users})


def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, "admin_page.html", {"reviews": reviews})


def request_list(request):
    requests = RequestModel.objects.all()
    return render(request, "admin_page.html", {"requests": requests})


@login_required
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == "POST":
        message = request.POST.get("message")
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You answer questions."},
                    {"role": "user", "content": message},
                ],
            )
            bot_response = response.choices[0].message.content.strip()

            chat = Chat(
                user=request.user,
                message=message,
                response=bot_response,
                created_at=timezone.now(),
            )
            chat.save()

            return JsonResponse({"message": message, "response": bot_response})
        except Exception as e:
            print(f"Error in chatbot view: {e}")
            return JsonResponse(
                {"error": "An error occurred while processing your request."},
                status=500,
            )

    return render(request, "chatbot.html", {"chats": chats})


def Request(request):
    return render(request, "request_a_project.html")


def gallery(request):
    cards = CreateCard.objects.all().order_by("header")
    grouped_cards = {}
    for header, group in groupby(cards, key=lambda x: x.header):
        grouped_cards[header] = list(group)
    return render(request, "gallery.html", {"cards": grouped_cards})


def index(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
        else:
            pass
    else:
        form = ReviewForm()

    return render(request, "index.html", {"form": form})


def pricing(request):
    return render(request, "pricing.html")


def signUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "signUp.html", {"form": form})


def signIn(request):
    password_error = False

    if request.method == "POST":
        if "signin" in request.POST:
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("index")
                else:
                    messages.error(request, "Invalid username or password.")
        elif "signup" in request.POST:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if password1 != password2:
                password_error = True
                messages.error(request, "Passwords do not match. Please try again.")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1
                )
                login(request, user)
                return redirect("index")

    form_signin = AuthenticationForm()
    form_signup = UserCreationForm()
    return render(
        request,
        "signIn.html",
        {
            "form_signin": form_signin,
            "form_signup": form_signup,
            "password_error": password_error,
        },
    )


def signOut(request):
    logout(request)
    return redirect("index")


def Assembly(request):
    return render(request, "Assembly.html")


def admin(request):
    return render(request, "admin_page.html")


def Carpenter(request):
    return render(request, "Carpenter.html")


def Home_Repairs(request):
    return render(request, "Home_Repairs.html")


def Installation(request):
    return render(request, "Instulation.html")


def More_About_Me(request):
    return render(request, "More_About_Me.html")


def Moving(request):
    return render(request, "Moving.html")


def Outdoor_Help(request):
    return render(request, "Outdoor_Help.html")


def Painting(request):
    return render(request, "Painting.html")


def admin_page(request):
    return render(request, "admin_page.html")


def submit_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        print("POST Data:", request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("index")
        else:
            pass
    else:
        form = ReviewForm()

    return render(request, "submit_review.html", {"form": form})


def reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def card(request):
    form = CreateCardForm()
    if request.method == "POST":
        form = CreateCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "create.html", {"form": form})
    return render(request, "create.html", {"form": form})
