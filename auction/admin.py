from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bid

class BidAdmin(admin.ModelAdmin):
    list_display = ('profile', 'user', 'bid_price', 'timestamp', 'is_winner')
    list_filter = ('profile', 'is_winner')
    search_fields = ('user__username', 'profile__name')

admin.site.register(Bid, BidAdmin)
