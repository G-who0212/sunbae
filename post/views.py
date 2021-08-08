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
    return render(request, 'detail.html', {'post':post})