from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import authenticate,login

from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if  request.method=="POST":
        user_name=request.POST.get("username","")
        pass_word=request.POST.get("password","")
        user=authenticate(request,username=user_name,password=pass_word)
        if user is not None:
            login(request,user.user_name,user.pass_word)
            return render(request,'index.html')

        else:
            return render(request,'login.html',{'error':'非法登录'})

    elif request.method=="GET":
        return render(request,"login.html",{})