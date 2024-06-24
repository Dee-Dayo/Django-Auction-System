from django.contrib import admin
from .models import Item, User


# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'item_name', 'item_amount', 'item_category', 'item_status']


@admin.register(User)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'role', 'is_logged_in']
