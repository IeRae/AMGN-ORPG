from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request,'testPage/index.html', {})

def room(requset, userName, roomName):
    return render(requset, 'testPage/room.html',{
        'room_name_json': mark_safe(json.dumps(roomName)),
        'user_name_json': mark_safe(json.dumps(userName))
    })