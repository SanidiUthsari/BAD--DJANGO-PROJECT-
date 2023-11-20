# auction/models.py
from django.db import models
from django.conf import settings  # Import settings module

class Bid(models.Model):
    profile = models.ForeignKey('showroom.Profile', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.profile.name} Bid'
