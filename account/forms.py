from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from .models import Career, Univ


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'profile_image', 'name', 'major', 'studentNum', 'campus', 'schoolEmail', 'websiteName', 'websiteURL']
        # 'career1Company', 'career1Title', 'career1YearStart', 'career1MonthStart', 'career1YearEnd', 'career1MonthEnd', 'career1RoleAchievement', 'university1Activity', 'university1Title', 'university1YearStart', 'university1MonthStart', 'university1YearEnd', 'university1MonthEnd', 'university1RoleAchievement', 'websiteName', 'websiteURL']

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['company', 'title', 'careerYearStart', 'careerMonthStart', 'careerYearEnd', 'careerMonthEnd', 'careerRoleAchievement']

class UnivForm(forms.ModelForm):
    class Meta:
        model = Univ
        fields = ['universityActivity', 'universityTitle', 'university_YearStart', 'university_MonthStart', 'university_YearEnd', 'university_MonthEnd', 'university_RoleAchievement']

class ChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'name', 'major', 'studentNum', 'campus', 'schoolEmail', 'websiteName', 'websiteURL']