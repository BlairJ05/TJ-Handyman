from django.urls import path
from .views import index, signUp,signIn,signUp,signOut,Assembly,Carpenter,Home_Repairs,Installation,More_About_Me,Moving,Outdoor_Help,Painting,pricing,gallery,Request

urlpatterns = [
    path('', index, name='index'),
    path('signUp/',signUp, name='signUp'),
    path('signIn/',signIn, name='signIn'),
    path('signUp/',signUp, name='signUp'),
    path('signOut/',signOut, name='signOut'),
    path('Assembly/',Assembly, name='Assembly'),
    path('Carpenter/',Carpenter, name='Carpenter'),
    path('Home_Repairs/',Home_Repairs, name='Home_Repairs'),
    path('Installation/',Installation, name='Installation'),
    path('More_About_Me/',More_About_Me, name='More_About_Me'),
    path('Moving/',Moving, name='Moving'),
    path('Painting/',Painting, name='Painting'),
    path('Outdoor_Help/',Outdoor_Help, name='Outdoor_Help'),
    path('pricing/',pricing,name='pricing'),
    path('gallery/',gallery,name='gallery'),
    path('request_a_project/',Request,name='request_a_project'),





]
