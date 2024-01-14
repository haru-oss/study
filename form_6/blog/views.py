from django.shortcuts import render

# Create your views here.


def index(request):

    params={"name":"しもつ"}
    
    return render(request,"blog/index.html",params)