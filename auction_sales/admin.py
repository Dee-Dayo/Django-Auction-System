from django.contrib import admin
from .models import Item


# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'item_name', 'item_amount', 'item_category', 'item_status']
