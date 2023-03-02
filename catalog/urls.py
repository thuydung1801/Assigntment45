from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name = "catalog_home"),
    path("category/<str:category_slug>/", views.show_category, name = "catalog_category"),
    path("product/<str:product_slug>/", views.show_product, name = "catalog_product"),
]
