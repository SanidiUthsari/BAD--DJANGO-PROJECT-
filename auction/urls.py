# auction/urls.py
from django.urls import path
from .views import profile_list, profile_detail, place_bid

app_name = "auction"

urlpatterns = [
    path('profiles/', profile_list, name='profile_list'),
    path('profiles/<int:profile_id>/', profile_detail, name='profile_detail'),
    path('profiles/<int:profile_id>/bid/', place_bid, name='place_bid'),
]
