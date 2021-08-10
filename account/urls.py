from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('registerCareer/', register_view_career, name="registerCareer"),
    path('registerUniv/', register_view_univ, name="registerUniv"),
    path('mypage/', mypage, name="mypage"),
    path('<int:pk>/follow/',follow, name="follow"),
    path('<int:pk>/seefollow/',seefollow,name="seefollow"),
    path('otherpage/<str:id>', otherpage, name="otherpage"),
    path('chaneInfo/', change_info, name="changeInfo"),
    path('withdraw/', withdraw, name="withdraw"),
    path('changePW/', change_password, name="changePW"),
]