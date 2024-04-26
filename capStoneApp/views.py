from itertools import groupby
from django.shortcuts import render, redirect
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
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Chat
from django.http import JsonResponse
from django.contrib import messages
from openai import OpenAI
from django.utils import timezone
from django.http import JsonResponse
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

client = OpenAI(api_key="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")

# views.py


def get_analytics_data(request):
    credentials = Credentials.from_authorized_user_info(
        request.session["google_credentials"],
        scopes=["https://www.googleapis.com/auth/analytics.readonly"],
    )

    analytics = build("analyticsreporting", "v4", credentials=credentials)

    response = (
        analytics.reports()
        .batchGet(
            body={
                "reportRequests": [
                    {
                        "viewId": "YOUR_VIEW_ID",
                        "dateRanges": [{"startDate": "7daysAgo", "endDate": "today"}],
                        "metrics": [
                            {"expression": "ga:sessions"},
                            {"expression": "ga:pageviews"},
                        ],
                    }
                ]
            }
        )
        .execute()
    )

    analytics_data = {
        "totalVisitors": response["reports"][0]["data"]["totals"][0]["values"][0],
        "pageViews": response["reports"][0]["data"]["totals"][0]["values"][1],
    }

    return JsonResponse(analytics_data)


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
            form = UserCreationForm(request.POST)
            if form.is_valid():
                if form.cleaned_data["password1"] != form.cleaned_data["password2"]:
                    password_error = True
                    messages.error(request, "Passwords do not match. Please try again.")
                else:
                    form.save()
                    username = form.cleaned_data.get("username")
                    password = form.cleaned_data.get("password1")
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect("index")
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")

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
