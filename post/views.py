from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.http import HttpResponse
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .models import Post, Comment
from .forms import PostForm
from account.models import CustomUser
from operator import itemgetter

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # 자신이 팔로우 한 사람들의 최신글 + 최신글을 20개까지 가져오기
    following_list = request.user.followings.all()
    post_list = []
    for following in following_list:
        post_list += list(Post.objects.filter(author = following))
    cnt = len(post_list)
    if cnt < 20:
        all_posts = Post.objects.order_by('-pub_date')
        for post in all_posts:
            if post not in post_list:
                post_list.append(post)
                cnt += 1
            if cnt >= 20:
                break
    else:
        # 최신 20개 글만 가져오기
        post_list.sort(key=itemgetter('pub_date'), reverse=True)
        post_list = post_list[:20]
        
    return render(request, 'home.html', {'post_list':post_list})

def new(request):
    post = PostForm()
    return render(request, 'new.html', {'post':post})

def create(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.pub_date = timezone.now()
        if request.user.is_authenticated:
            new_post.author = request.user
            new_post.save()
            return redirect('detail', new_post.id)
    return redirect('home')

def update(request, id):
    post = get_object_or_404(Post, pk = id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', post.id)
        else:
            return redirect('home')
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'post':form,'postmodel':post})

def delete(request, id):
    delete_post = get_object_or_404(Post, pk = id)
    delete_post.delete()
    return redirect('home')

def detail(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post = id).order_by('pub_date')
    return render(request, 'detail.html', {'post':post, 'comments':comments})

# comment view
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    writer_id = request.POST.get('writer_id')
    writer = get_object_or_404(CustomUser, pk = writer_id)
    content = request.POST.get('content')
    
    comment = Comment.objects.create(post = post, user = writer, content = content)
    comment.save()
    response = {
        'comment_id': comment.id,
        'writer_profile_image': writer.profile_image.url,
        'writer_name': writer.name,
        'writer_major': writer.major,
        'writer_studentNum': writer.studentNum,
        'content': content,
        'pub_date': comment.pub_date
    }

    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type = "application/json")

def comment_delete(request, post_id):
    comment_id = request.POST.get('comment_id')
    delete_comment = Comment.objects.get(pk = comment_id)
    delete_comment.delete()
    response = {
        'message': '성공적으로 삭제되었습니다.'
    }
    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type = "application/json")
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