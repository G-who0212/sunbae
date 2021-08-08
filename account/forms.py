from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'profile_image', 'name', 'major', 'studentNum', 'campus', 'schoolEmail']
        # 'career1Company', 'career1Title', 'career1YearStart', 'career1MonthStart', 'career1YearEnd', 'career1MonthEnd', 'career1RoleAchievement', 'university1Activity', 'university1Title', 'university1YearStart', 'university1MonthStart', 'university1YearEnd', 'university1MonthEnd', 'university1RoleAchievement', 'websiteName', 'websiteURL']


