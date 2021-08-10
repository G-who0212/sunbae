from account.models import CustomUser
from django.shortcuts import get_object_or_404, render, redirect


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm#, UserCreationForm
from django.contrib.auth import authenticate, login, logout,get_user_model, update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from .forms import CareerForm, RegisterForm, UnivForm, ChangeForm
from post.forms import PostForm
from post.models import Post
from account.models import CustomUser, Career, Univ
from django.contrib.auth.forms import PasswordChangeForm

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
        form = RegisterForm(request.POST, request.FILES) #request.FILES추가
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            return redirect("registerCareer")
        else:
            return render(request, 'invalid_password.html')
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
                career.user = request.user 
                career = form.save()
        return redirect("registerCareer")
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
        return redirect("registerUniv")
    else:
        form = UnivForm()
        return render(request, 'signupUniv.html', {'form':form})        


# def mypage(request):
#     return render(request,'myprofile.html')

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


def mypage(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user).order_by('-pub_date')
        careers = Career.objects.filter(user=request.user)
        univs = Univ.objects.filter(user=request.user)
        return render(request,'myprofile.html', {'posts':posts, 'careers':careers, 'univs':univs})
    else:
        return render(request, 'ifNotAuthenticated.html')


def otherpage(request, id):
    post = get_object_or_404(Post, pk=id)
    author = post.user
    aID = post.user.id
    customuser = get_object_or_404(CustomUser, pk=aID)
    posts = Post.objects.filter(user=author).order_by('-pub_date')
    careers = Career.objects.filter(user=author)
    univs = Univ.objects.filter(user=author)
    return render(request, 'otherprofile.html', {'customuser':customuser, 'posts':posts, 'careers':careers, 'univs':univs})


def change(request):
    if request.method == 'POST': 
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            if username == request.user.username:
                password = form.cleaned_data.get("password")
                user = authenticate(request=request, username=username, password=password)
                if user is not None:
                    return render(request, 'change.html')
            else:
                return render(request, 'wrongIDorPW.html')   
        else:
             return render(request, 'wrongIDorPW.html')
        return redirect("home")
    else:
        form = AuthenticationForm()
        return render(request, 'doubleCheck.html', {'form':form})


def change_info(request):
    if request.method == "POST":
        form = ChangeForm(request.POST, request.FILES, instance=request.user) #request.FILES추가
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect("home")
    else:
        form = ChangeForm(instance=request.user)
        # form = UserCreationForm()
        return render(request, 'changeInfo.html', {'form':form})

def withdraw(request):
    request.user.delete()
    return redirect("home")

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #비밀번호가 수정되서 자동으로 로그아웃이 되는 것을 방지하기 위해서 변경된 정보를 세션에 바로 업데이트
            return redirect("home")
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'changePassword.html', {'form':form})

#careers = Career.objects.filter(id=request.user.id)
def career_show(request):
    careers = Career.objects.filter(user=request.user)
    return render(request, 'careerShow.html', {'careers':careers})

def career_edit(request, id):
    career = get_object_or_404(Career, pk=id)

    if request.method == 'POST':
	    form = CareerForm(request.POST, instance=career)
	    if form.is_valid():
		    career = form.save()
		    return redirect("home")
    else:
	    form = CareerForm(instance=career)
    return render(request, 'signUpCareer.html', {'form':form})

def university_show(request):
    univs = Univ.objects.filter(user=request.user)
    return render(request, 'universityShow.html', {'univs':univs})

def university_edit(request, id):
    univ = get_object_or_404(Univ, pk=id)

    if request.method == 'POST':
	    form = UnivForm(request.POST, instance=univ)
	    if form.is_valid():
		    univ = form.save()
		    return redirect("home")
    else:
	    form = UnivForm(instance=univ)
    return render(request, 'signUpUniv.html', {'form':form})