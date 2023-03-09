from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_checkout, name = "checkout"),
    path("receipt/", views.receipt, name = "receipt"),
]
