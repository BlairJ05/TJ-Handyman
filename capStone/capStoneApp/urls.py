from django.urls import path
from .views import index, signUp,signIn

urlpatterns = [
    path('', index, name='index'),
    path('signUp/',signUp, name='signUp'),
    path('signIn/',signIn, name='signIn'),
]
