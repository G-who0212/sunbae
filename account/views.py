from account.models import CustomUser
from django.shortcuts import get_object_or_404, render, redirect


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm#, UserCreationForm
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth import authenticate, login, logout
from .forms import CareerForm, RegisterForm, UnivForm
from post.forms import PostForm
from post.models import Post
from account.models import CustomUser, Career, Univ

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST': 
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
        else:
             return render(request, 'wrongIDorPW.html')
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
        return redirect("registerCareer")
    else:
        form = RegisterForm()
        # form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})

def register_view_career(request):
    if request.method == "POST":
        form = CareerForm(request.POST)
        if form.is_valid():
            career = form.save(commit=False)
            if request.user.is_authenticated:
                career.user = request.user #잘못된 이유를 모르겠음
                career = form.save()
        return redirect("registerUniv")
    else:
        form = CareerForm()
        return render(request, 'signupCareer.html', {'form':form})


def register_view_univ(request):
    if request.method == "POST":
        form = UnivForm(request.POST)
        if form.is_valid():
            univ = form.save(commit=False)
            if request.user.is_authenticated:
                univ.user = request.user 
                univ = form.save()
        return redirect("home")
    else:
        form = UnivForm()
        return render(request, 'signupUniv.html', {'form':form})        


def profile(request, id):
    user = get_object_or_404(CustomUser,pk=id)
    follower_list = user.followers.all()
    following_list = user.followings.all()
    career_list = Career.objects.filter(user = id)
    univ_list = Univ.objects.filter(user = id)
    post_list = Post.objects.filter(author = id)
    return render(request,'profile.html', {'user':user, 'follower_list':follower_list, 'following_list':following_list, 'career_list':career_list, 'univ_list':univ_list, 'post_list':post_list})

def follow(request,pk):
    CustomUser = get_user_model()
    user = get_object_or_404(CustomUser,pk=pk)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    return redirect('profile',user.pk)


def seefollow(request,pk):
    CustomUser = get_user_model()
    user = get_object_or_404(CustomUser,pk=pk)
    followings=user.followings.all()
    followers=user.followers.all()
    return render (request,'follow.html',{'followings':followings},{'followers':followers})



    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user).order_by('-pub_date')
        careers = Career.objects.filter(user=request.user)
        univs = Univ.objects.filter(user=request.user)
        return render(request,'profile.html', {'posts':posts, 'careers':careers, 'univs':univs})
    else:
        return render(request, 'ifNotAuthenticated.html')