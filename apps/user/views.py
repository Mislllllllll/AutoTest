from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.backends import ModelBackend

# Create your views here.
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.views.generic.base import View

from .forms import LoginForm,RegisterForm

# Create your views here.
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class RegisterView(View):
    def get(self,request):
        register_form=RegisterForm
        return render(request,"register.html")

class LoginView(View):
    def get(self,request):
        return render(request, "login.html", {})
    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():

            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(request, username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})

        else:
            return render(request, 'login.html', {"login_form":login_form})



##该方法可删除
def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')

        else:
            return render(request, 'login.html', {'error': '非法登录'})

    elif request.method == "GET":
        return render(request, "login.html", {})



