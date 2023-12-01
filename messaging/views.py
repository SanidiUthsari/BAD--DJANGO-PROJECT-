from django.shortcuts import render

# Create your views here.
# messaging/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from django.contrib.auth.models import User


# messaging/views.py

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user, is_read=False)
    print(received_messages)  # Add this line for debugging
    return render(request, 'messaging/inbox.html', {'received_messages': received_messages})



# messaging/views.py

@login_required
def send_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)

    if request.method == 'POST':
        content = request.POST.get('content', '')
        print(request.user, receiver, content)  # Add this line for debugging
        if content:
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            messages.success(request, f'Message sent to {receiver.username}')
        else:
            messages.error(request, 'Message content cannot be empty')

    return render(request, 'messaging/send_message.html', {'receiver': receiver})
