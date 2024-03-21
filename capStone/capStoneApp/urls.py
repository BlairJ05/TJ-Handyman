from django.urls import path
from .views import index, signUp,signIn,signUp,signOut

urlpatterns = [
    path('', index, name='index'),
    path('signUp/',signUp, name='signUp'),
    path('signIn/',signIn, name='signIn'),
    path('signUp/',signUp, name='signUp'),
    path('signOut/',signOut, name='signOut'),


]
