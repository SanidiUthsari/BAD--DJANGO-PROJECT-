from django.shortcuts import render

# Create your views here.
# auction/views.py
from django.shortcuts import render, get_object_or_404
from .models import Bid
from showroom.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect



def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'auction/profile_list.html', {'profiles': profiles})

def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'auction/profile_detail.html', {'profile': profile})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Bid
from showroom.models import Profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='account:login')
def place_bid(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    if request.method == 'POST':
        bid_price = request.POST.get('bid_price')
        # Validate bid_price and handle the bidding logic

        Bid.objects.create(profile=profile, user=request.user, bid_price=bid_price)

        # Determine the winning bid
        winning_bid = Bid.objects.filter(profile=profile).order_by('-bid_price').first()

        # Mark the winning bid
        if winning_bid:
            winning_bid.is_winner = True
            winning_bid.save()

        # Redirect to a success page or back to the profile details page
        return redirect('auction:profile_list')

    return render(request, 'auction/place_bid.html', {'profile': profile})
