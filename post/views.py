from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'home.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'new.html', {'post':post})

def new(request):
    post = PostForm()
    return render(request, 'new.html', {'post':post})

def create(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.pub_date = timezone.now()
        new_post.writer = request.POST['name']
        new_post.major = request.POST['major']
        new_post.career1Title = request.POST['career']
        new_post.save()
        return redirect('detail', new_post.id)
    return redirect('home')

def edit(request, id):
    post = Post.objects.get(id = id)
    edit_post = PostForm(value=post)
    return render(request, 'edit.html',{'post':edit_post})

def update(request, id):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        update_post = form.save(commit=False)
        update_post.pub_date = timezone.now()
        update_post.save()
        return redirect('detail', update_post.id)
    return redirect('home')

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('home')

def detail(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'detail.html', {'post':post})

from django.http import HttpResponse,JsonResponse
import json
    
def likes(request): 
    if request.is_ajax(): #ajax 방식일 때 아래 코드 실행
        post_id = request.GET['post_id'] #좋아요를 누른 게시물id (post_id)가지고 오기
        post = Post.objects.get(id=post_id) 
				
        if not request.user.is_authenticated: #버튼을 누른 유저가 비로그인 유저일 때
            message = "로그인을 해주세요" #화면에 띄울 메세지 
            context = {'like_count' : post.like.count(),"message":message}
            return HttpResponse(json.dumps(context), content_type='application/json')

        user = request.user #request.user : 현재 로그인한 유저
        if post.like.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
            post.like.remove(user) #like field에 현재 유저 추가
            message = "좋아요 취소" #화면에 띄울 메세지
        else: #좋아요를 누르지 않은 유저일 때
            post.like.add(user) #like field에 현재 유저 삭제
            message = "좋아요" #화면에 띄울 메세지
        # post.like.count() : 게시물이 받은 좋아요 수  
        context = {'like_count' : post.like.count(),"message":message}
        return HttpResponse(json.dumps(context), content_type='application/json')    