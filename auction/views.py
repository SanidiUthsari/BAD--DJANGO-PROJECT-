from django.shortcuts import render

# Create your views here.
# auction/views.py
from django.shortcuts import render, get_object_or_404
from .models import Bid
from showroom.models import Profile

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'auction/profile_list.html', {'profiles': profiles})

def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'auction/profile_detail.html', {'profile': profile})

def place_bid(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    if request.method == 'POST':
        bid_price = request.POST.get('bid_price')
        # Validate bid_price and handle the bidding logic

        Bid.objects.create(profile=profile, user=request.user, bid_price=bid_price)
        # Redirect to a success page or back to the profile details page

    return render(request, 'auction/place_bid.html', {'profile': profile})
