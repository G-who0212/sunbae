from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>',detail,name="detail"), 
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('detail/<str:id>', detail, name="detail"),
    path('detail/<str:post_id>/comment/create', comment_create, name="comment_create"),
    path('detail/<str:post_id>/comment/delete', comment_delete, name="comment_delete"),
    path('like/', likes, name="likes"),
]