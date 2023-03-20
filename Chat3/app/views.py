from django.shortcuts import render
from .models import Group,Chat

def Home(request,groupkaname):
    group = Group.objects.filter(name = groupkaname).first()
    chat =[]
    if not group:
        group = Group.objects.create(name = groupkaname)
    chats = Chat.objects.filter(group = group)
    return render(request,'index.html',{'groupkaname':groupkaname,'chats':chats})