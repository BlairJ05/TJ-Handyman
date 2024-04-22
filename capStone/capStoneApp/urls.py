from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("signIn/", views.signIn, name="signIn"),
    path("signOut/", views.signOut, name="signOut"),
    path("Assembly/", views.Assembly, name="Assembly"),
    path("Carpenter/", views.Carpenter, name="Carpenter"),
    path("Home_Repairs/", views.Home_Repairs, name="Home_Repairs"),
    path("Installation/", views.Installation, name="Installation"),
    path("More_About_Me/", views.More_About_Me, name="More_About_Me"),
    path("Moving/", views.Moving, name="Moving"),
    path("Painting/", views.Painting, name="Painting"),
    path("Outdoor_Help/", views.Outdoor_Help, name="Outdoor_Help"),
    path("pricing/", views.pricing, name="pricing"),
    path("gallery/", views.gallery, name="gallery"),
    path("request_a_project/", views.Request, name="request_a_project"),
    path("submit_review/", views.submit_review, name="submit_review"),
    path("reviews/", views.reviews, name="rating"),
    path("reviews/", views.reviews, name="reviews"),
    path("accounts/login/", views.signIn, name="login"),
    path("create_card/", views.card, name="create_card"),
    path("admin_page/", views.admin_page, name="admin_page"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
