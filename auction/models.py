# auction/models.py
from django.db import models
from django.conf import settings  # Import settings module

class Bid(models.Model):
    profile = models.ForeignKey('showroom.Profile', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=15, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return f"Bid by {self.user.username} on {self.profile.name}"
    
    @classmethod
    def get_highest_bid(cls, profile):
        return cls.objects.filter(profile=profile).order_by('-bid_price').first()
