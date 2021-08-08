from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('registerCareer/', register_view_career, name="registerCareer"),
    path('registerUniv/', register_view_univ, name="registerUniv"),
    path('mypage/', mypage, name="mypage"),
    path('otherpage/<str:id>', otherpage, name="otherpage"),
]