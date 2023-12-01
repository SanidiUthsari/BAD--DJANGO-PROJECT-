# messaging/urls.py
from django.urls import path
from .views import inbox, send_message

app_name = 'messaging'

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('send_message/<int:receiver_id>/', send_message, name='send_message'),
]
