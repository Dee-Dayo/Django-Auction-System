from django.urls import path
from . import views

urlpatterns = [
    path('auction', views.list_items),
    path('auction/seller', views.list_seller),
]
