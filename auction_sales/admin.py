from django.contrib import admin
from .models import Item
from .models import User


# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'item_name', 'item_amount', 'item_category', 'item_status']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'email', 'username', 'password']
