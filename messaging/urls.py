
# messaging/urls.py
from django.urls import path
from .views import inbox, send_message, view_conversation

app_name = 'messaging'

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('send_message/<int:receiver_id>/', send_message, name='send_message'),
    path('view_conversation/<int:receiver_id>/', view_conversation, name='view_conversation'),
]
