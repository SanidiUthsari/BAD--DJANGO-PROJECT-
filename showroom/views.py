from django.shortcuts import render , redirect
from .models import Profile
from .forms import ContactForm , ProfileForm
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required


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

@login_required
def newView(request):
    profile_formset = formset_factory(ProfileForm, extra=1)

    if request.method == 'POST':
        formset = profile_formset(request.POST, request.FILES)

        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                  
                    form.save()

            return redirect('showroom:home_list')  # Corrected line

    else:
        formset = profile_formset()

    return render(request, 'showroom/new_profile.html', {'formset': formset})
    
    