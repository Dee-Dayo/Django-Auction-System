from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.


class Item(models.Model):
    item_id = models.CharField(primary_key=True, unique=True, max_length=100)
    item_name = models.CharField(max_length=100, null=False, blank=False)
    ITEM_CATEGORY = [
        ('F', 'FURNITURE'),
        ('E', 'ELECTRONICS'),
        ('FASH', 'FASHION'),
        ('A', 'ANTIQUES'),
        ('AR', 'ART'),
        ('B', 'BOOK'),
        ('JEW', 'JEWELRY'),
        ('S', 'SPORT'),
        ('W', 'WINE')
    ]
    ITEM_STATUS = [
        ('UP', 'UPCOMING'),
        ('ON', 'ONGOING'),
        ('CL', 'CLOSED')
    ]
    item_amount = models.DecimalField(max_digits=10, decimal_places=2)
    item_category = models.CharField(max_length=4, choices=ITEM_CATEGORY, default='A', null=False, blank=False)
    item_status = models.CharField(max_length=2, choices=ITEM_STATUS, default='UP', null=False, blank=False)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)


class Bid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bids")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

