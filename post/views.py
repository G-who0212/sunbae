from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.http import HttpResponse
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .models import Post, Comment
from .forms import PostForm
from account.models import CustomUser

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
        if request.user.is_authenticated:
            new_post.user = request.user
            new_post.aID = request.user.id
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
        'writer_name': writer.name,
        'writer_major': writer.major,
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