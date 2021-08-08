from account.models import CustomUser
from django.shortcuts import get_object_or_404, render, redirect


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm#, UserCreationForm
from django.contrib.auth import authenticate, login, logout,get_user_model
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST': #Blog앱에서 두개의 메소드로 나누었던 것을 하나의 메소드로 합침(DB의 내용에 접근할때 request.method의 방식이 달라지는 것을 활용함)
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)

        return redirect("home")
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    else:
        form = RegisterForm()
        # form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})


def mypage(request):
    return render(request,'myprofile.html')

def follow(request,pk):
    CustomUser = get_user_model()
    user = get_object_or_404(CustomUser,pk=pk)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    return redirect('myprofile',user.pk)


def seefollow(request,pk):
    CustomUser = get_user_model()
    user = get_object_or_404(CustomUser,pk=pk)
    followings=user.followings.all()
    followers=user.followers.all()
    return render (request,'follow.html',{'followings':followings},{'followers':followers})


