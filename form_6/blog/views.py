from django.shortcuts import render

from .models import Friends



def index(request):


    data=Friends.objects.all()
    
    params={
        'title':"hello",
        'mesagge':"all friends",
        'data':data,
    }
    
    
    return render(request,'blog/index.html',params)