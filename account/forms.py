from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserCreationForm
from .models import CustomUser
from django import forms
from .models import Career, Univ



class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'profile_image', 'name', 'major', 'studentNum', 'campus', 'schoolEmail', 'websiteName', 'websiteURL']
        labels = {'username':'아이디','profile_image':'프로필 사진','name':'이름','major':'전공','studentNum':'학번','campus': '캠퍼스','schoolEmail':'학교 이메일','websiteName':'웹사이트 이름','websiteURL':'웹사이트 URL'}


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['company', 'title', 'careerYearStart', 'careerMonthStart', 'careerYearEnd', 'careerMonthEnd']
        labels = {'company': '회사', 'title':'직함', 'careerYearStart':'시작 연도', 'careerMonthStart':'시작 월', 'careerYearEnd':'종료 연도', 'careerMonthEnd':'종료 월'}

class UnivForm(forms.ModelForm):
    class Meta:
        model = Univ
        fields = ['universityActivity', 'universityTitle', 'university_YearStart', 'university_MonthStart', 'university_YearEnd', 'university_MonthEnd']
        labels = {'universityActivity': '대학생 활동', 'universityTitle':'직함', 'university_YearStart':'시작 연도', 'university_MonthStart':'시작 월', 'university_YearEnd':'종료 연도', 'university_MonthEnd':'종료 월'}

class ChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'name', 'major', 'studentNum', 'campus', 'schoolEmail', 'websiteName', 'websiteURL']
        labels = {'profile_image': '프로필 사진', 'name': '이름', 'major': '전공', 'studentNum': '학번', 'campus': '캠퍼스', 'schoolEmail': '학교 이메일', 'websiteName': '웹사이트 이름', 'websiteURL': '웹사이트 URL'}