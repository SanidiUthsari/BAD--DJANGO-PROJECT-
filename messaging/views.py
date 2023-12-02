# messaging/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Message

@login_required
def inbox(request):
    senders = User.objects.exclude(id=request.user.id)
    latest_messages = {}
    for sender in senders:
        latest_message = Message.objects.filter(
            Q(sender=request.user, receiver=sender) | Q(sender=sender, receiver=request.user)
        ).order_by('-timestamp').first()

        latest_messages[sender] = latest_message

    return render(request, 'messaging/inbox.html', {'latest_messages': latest_messages})

@login_required
def send_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)

    message_thread = Message.objects.filter(
        Q(sender=request.user, receiver=receiver) | Q(sender=receiver, receiver=request.user)
    ).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content:
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            messages.success(request, f'Message sent to {receiver.username}')
            return redirect('messaging:inbox')
        else:
            messages.error(request, 'Message content cannot be empty')

    return render(request, 'messaging/send_message.html', {'receiver': receiver, 'message_thread': message_thread})

@login_required
def view_conversation(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)

    message_thread = Message.objects.filter(
        Q(sender=request.user, receiver=receiver) | Q(sender=receiver, receiver=request.user)
    ).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content:
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            messages.success(request, f'Message sent to {receiver.username}')
            return redirect('messaging:view_conversation', receiver_id=receiver.id)
        else:
            messages.error(request, 'Message content cannot be empty')

    return render(request, 'messaging/view_conversation.html', {'receiver': receiver, 'message_thread': message_thread})
