from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>',detail,name="detail"), 
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('detail/<int:id>', detail, name="detail"),

    path('like/', likes, name="likes"),
]