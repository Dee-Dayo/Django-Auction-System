from rest_framework import serializers
from .models import Item, Bid


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'item_amount', 'item_category', 'start_date', 'end_date', 'seller']


