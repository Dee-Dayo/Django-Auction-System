from rest_framework import serializers
from .models import Item, Bid


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_id', 'item_name', 'item_amount', 'item_category', 'item_status']


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['item_name', 'item_category', 'starting_price', 'start_date', 'end_date', 'bidder']
