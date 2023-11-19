from django.urls import path
from . import views


app_name = 'showroom'

urlpatterns = [
    path('', views.profileListView, name='home_list'),
    path('<int:Profile_id>', views.profiledetailView, name='profiles'),
    path('contact/', views.ContactView, name='contact'),
    path('new_profile', views.newView, name='new_profile'),
]
