from django.contrib import admin
from .models import Item, Bid


# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'item_name', 'item_amount', 'item_category', 'item_status']


@admin.register(Bid)
class Bid(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'bidder', 'item_category', 'starting_price',
                    'start_date', 'end_date']


@admin.register(Bid)
class Bid(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'bidder', 'item_category', 'starting_price',
                    'start_date', 'end_date']