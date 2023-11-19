from django.contrib import admin
from .models import Profile




class ProfileAdmin(admin.ModelAdmin):
    list_display=('name','id', 'variant')
    list_display_links=('name',)
    list_filter = ('year','name','price')
    search_fields= ('insured',)

admin.site.register(Profile, ProfileAdmin)
