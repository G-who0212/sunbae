from account.models import CustomUser
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout,get_user_model, update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from .forms import CareerForm, RegisterForm, UnivForm, ChangeForm
from post.forms import PostForm
from post.models import Post
from account.models import CustomUser, Career, Univ
from django.contrib.auth.forms import PasswordChangeForm
import jwt
import json
from sproject.email_settings import SECRET_KEY
from .emailText import message
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text

# Create your views here.
def login_view(request):
    if request.method == 'POST': 
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("home")
        else:
             return render(request, 'wrongIDorPW.html')
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

            current_site = get_current_site(request)
            domain = current_site.domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))
            token = jwt.encode({'user':user.id}, SECRET_KEY['secret'], SECRET_KEY['algorithm'])
            message_data = message(domain, uidb64, token)

            mail_title = "선배님 이메일 인증을 완료해주세요"
            mail_to = user.schoolEmail
            email = EmailMessage(mail_title, message_data, to=[mail_to])
            email.send()

            return redirect("registerCareer")
        else:
            return render(request, 'invalid_password.html')
    else:
        form = RegisterForm()
        # form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
        user_dic = jwt.decode(token, SECRET_KEY['secret'], SECRET_KEY['algorithm'])
        if user.id == user_dic["user"]:
            user.email_auth = True
            user.save()
            login(request, user) 
            return redirect("home")
    
        return JsonResponse({'message':'auth fail'}, status=400)
    except ValidationError:
        return JsonResponse({'message':'type_error'}, status=400)

    except KeyError:
        return JsonResponse({'message':'INVALID_KEY'}, status=400)

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

def register_view_career2(request):
    if request.method == "POST":
        form = CareerForm(request.POST)
        if form.is_valid():
            career = form.save(commit=False)
            if request.user.is_authenticated:
                career.user = request.user 
                career = form.save()
        return redirect("registerCareer2")
    else:
        form = CareerForm()
        return render(request, 'signupCareer2.html', {'form':form})
        
def go_change(request):
    return render(request, "change.html")

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
        
def register_view_univ2(request):
    if request.method == "POST":
        form = UnivForm(request.POST)
        if form.is_valid():
            univ = form.save(commit=False)
            if request.user.is_authenticated:
                univ.user = request.user 
                univ = form.save()
        return redirect("registerUniv2")
    else:
        form = UnivForm()
        return render(request, 'signupUniv2.html', {'form':form})      

def signupComplete(request):
    return render(request, 'signupComplete.html')

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

def see_follower(request,pk):
    CustomUser= get_user_model()
    user = get_object_or_404(CustomUser,pk=pk)
    if user != request.user:
        return render(request,'myfollower.html',{'user' :user})
    else:
        return render(request,'myfollower.html',{'user':request.user})

def see_following(request,pk):
    CustomUser= get_user_model()
    user = get_object_or_404(CustomUser,pk=pk)
    if user != request.user:
        return render(request,'myfollowing.html',{'user' :user})
    else:
        return render(request,'myfollowing.html',{'user':request.user})


def otherpage(request, id):
    post = get_object_or_404(Post, pk=id)
    author = post.author
    aID = author.id
    customuser = get_object_or_404(CustomUser, pk=aID)
    posts = Post.objects.filter(author=author).order_by('-pub_date')
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
                    return render(request, 'wrongIDorPW2.html')
            else:
                return render(request, 'wrongIDorPW2.html')   
        else:
             return render(request, 'wrongIDorPW2.html')
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
    return render(request, 'changeCareer.html', {'form':form, 'career':career})

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
    return render(request, 'changeUniv.html', {'form':form, 'univ':univ})