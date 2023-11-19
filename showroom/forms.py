from django import forms
from django.core.validators import EmailValidator
from .models import Profile


class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email = forms.CharField(),
    variant = forms.CharField(max_length=50)
    add = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = "__all__"    

