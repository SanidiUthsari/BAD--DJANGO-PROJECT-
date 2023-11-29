from django.shortcuts import render, redirect
from .models import Profile
from .forms import ContactForm , ProfileForm
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def profileListView(request):
    profiles = Profile.objects.all()
    return render( request, 'showroom/home_list.html', {'profiles' :profiles})

@login_required
def profiledetailView(request,Profile_id):
    profil = Profile.objects.get(id=Profile_id)
    return render (request ,'showroom/profiles.html',{'profile': profil})

def ContactView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"EMAIL: {form.cleaned_data['variant']}")
            print(f"MESSAGE: {form.cleaned_data['year']}")
    
    if request.method == 'GET':
        form = ContactForm()
    
    return render (request, 'showroom/contact.html', {'form':form})


    
# showroom/views.py
from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import ProfileForm
from .models import Profile

@login_required(login_url='account:login')
def newView(request):
    profile_formset = formset_factory(ProfileForm, extra=1)

    if request.method == 'POST':
        formset = profile_formset(request.POST, request.FILES)

        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    profile = form.save(commit=False)
                    profile.bid_start_date = form.cleaned_data['bid_start_date']
                    profile.bid_end_date = form.cleaned_data['bid_end_date']
                    profile.save()

            return redirect('showroom:home_list')

    else:
        formset = profile_formset()

    return render(request, 'showroom/new_profile.html', {'formset': formset})

def search_profiles(request):

    query_name = request.GET.get('query')
    query_year = request.GET.get('year')

    filtered_profiles = Profile.objects.all()

    if query_name:
        filtered_profiles = filtered_profiles.filter(Q(name__icontains=query_name) | Q(variant__icontains=query_name))

    if query_year:
        filtered_profiles = filtered_profiles.filter(year=query_year)


    return render(request, 'showroom/search_results.html',
              {'filtered_profiles': filtered_profiles, 'query_name': query_name, 'query_year': query_year})
    
def about_us_view(request):
    return render(request, 'showroom/Aboutus.html')
