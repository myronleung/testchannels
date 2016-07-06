from django.shortcuts import render
from ctest.models import *

# Create your views here.
def chatroom(request):
    room = Room.objects.get(id=1)
    messages = Message.objects.filter(room=room)
    context = {
        'room': room,
        'messages': messages,
    }
    return render(request, 'ctest/chatroom.html/', context)
