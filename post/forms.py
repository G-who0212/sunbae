from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'body', 'hashtag', 'image']
        labels = {'category':'카테고리', 'body': '내용', 'hashtag': '해시태그', 'image': '이미지'}