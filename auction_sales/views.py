from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Item, Bid
from .serializers import ItemSerializer
from .form import CustomUserCreationForm


# Create your views here.

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
