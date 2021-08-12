from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('registerCareer/', register_view_career, name="registerCareer"),
    path('registerUniv/', register_view_univ, name="registerUniv"),
    path('activate/<str:uidb64>/<str:token>', activate, name="active"),
    path('profile/<str:id>', profile, name="profile"),
    path('<int:pk>/follow/',follow, name="follow"),
    path('<int:pk>/see_follower/',see_follower, name="see_follower"),
    path('<int:pk>/see_following/',see_following, name="see_following"),
    path('otherpage/<str:id>', otherpage, name="otherpage"),
    path('chaneInfo/', change_info, name="changeInfo"),
    path('withdraw/', withdraw, name="withdraw"),
    path('changePW/', change_password, name="changePW"),
    path('change/', change, name="change"),
    path('careerEdit/<str:id>', career_edit, name="careerEdit"),
    path('careerShow/', career_show, name="careerShow"),
    path('univEdit/<str:id>', university_edit, name="univEdit"),
    path('univShow/', university_show, name="univShow"),
]