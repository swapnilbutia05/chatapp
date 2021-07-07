'''
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'channels/index.html', {})



def room(request, room_name):
    return render(request, 'channels/chatroom.html', {
        'room_name': room_name
    })
'''
