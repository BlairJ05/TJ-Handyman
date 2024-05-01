from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("signIn/", views.signIn, name="signIn"),
    path("signOut/", views.signOut, name="signOut"),
    path("gallery/", views.gallery, name="gallery"),
    path("request_a_project/", views.Request, name="request_a_project"),
    path("submit_review/", views.submit_review, name="submit_review"),
    path("reviews/", views.reviews, name="rating"),
    path("reviews/", views.reviews, name="reviews"),
    path("accounts/login/", views.signIn, name="login"),
    path("create_card/", views.card, name="create_card"),
    path("admin_page/", views.admin_page, name="admin_page"),
    path("create_card/", views.card, name="create_card"),
    path("chatbot/", views.chatbot, name="chatbot"),
    path("user-list/", views.user_list, name="user_list"),
    path("reviews-list/", views.reviews_list, name="reviews_list"),
    path("request-list/", views.request_list, name="request_list"),
    path("submit-form/", views.submit_form, name="submit_form"),
    path("more_user/<int:user_id>/", views.more_user, name="more_user"),
    path("more_request/<int:request_id>/", views.more_request, name="more_request"),
    path(
        "review/<int:review_id>/approve/", views.approve_review, name="approve_review"
    ),
    path(
        "change_status/<int:request_id>/<str:new_status>/",
        views.change_status,
        name="change_status",
    ),
    path("invoice_form/", views.invoice_form, name="invoice_form"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
