from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.conf import settings


class CustomUserCreationForm(UserCreationForm):
    # role = forms.ChoiceField(choices=settings.AUTH_USER_MODEL.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email',  'password1', 'password2')