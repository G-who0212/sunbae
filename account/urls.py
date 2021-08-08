from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('mypage/', mypage, name="mypage"),
    path('<int:pk>/follow/',follow, name="follow"),
    path('<int:pk>/seefollow/',seefollow,name="seefollow"),
]