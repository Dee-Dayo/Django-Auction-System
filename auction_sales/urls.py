from django.urls import path
from . import views

urlpatterns = [
    path('auction', views.list_items),
    path('auction/bid', views.list_bids)
]
