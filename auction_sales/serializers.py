from rest_framework import serializers
from .models import Item, User


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_id', 'item_name', 'item_amount', 'item_category', 'item_status']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
