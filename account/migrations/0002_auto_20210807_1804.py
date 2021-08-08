# Generated by Django 3.2.3 on 2021-08-07 09:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='career1Company',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='career1MonthEnd',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='career1MonthStart',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='career1RoleAchievement',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='career1Title',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='career1YearEnd',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='career1YearStart',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='university1Activity',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='university1MonthEnd',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='university1MonthStart',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='university1RoleAchievement',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='university1Title',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='university1YearEnd',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='university1YearStart',
        ),
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(related_name='_account_customuser_followers_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(related_name='_account_customuser_following_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='major',
            field=models.CharField(choices=[('CS', '컴퓨터공학과'), ('ME', '기계시스템디자인공학과'), ('NE', '신소재공학과'), ('CHE', '화학공학과'), ('CEE', '건설환경공학과'), ('EE', '전자전기공학부'), ('DE', '산업데이터공학과'), ('Law', '법학부'), ('Mus', '뮤지컬전공'), ('PM', '실용음악전공'), ('Ar', '건축학과'), ('IAr', '실내건축학과'), ('CE', '도시공학과'), ('Kor', '국어국문학과'), ('Eng', '영어영문학과'), ('Fra', '불어불문학과'), ('Ger', '독어독문학과'), ('ArtFm', '미술대학자율전공'), ('Art', '예술학과'), ('Sc', '조소과'), ('Pa', '회화과'), ('OPa', '동양화가'), ('En', '판화과'), ('Ed', '교육학과'), ('KEd', '국어교육과'), ('EEd', '영어교육과'), ('MEd', '수학교육과'), ('HEd', '역사교육과'), ('VD', '시각디자인학과'), ('InD', '산업디자인학과'), ('PG', '도예유리과'), ('WF', '목조형가구학과'), ('MD', '금속조형디자인과'), ('FD', '섬유미술패션디자인과'), ('Man', '경영학과'), ('Ec', '경제학과'), ('SFm', '서울캠퍼스자율전공'), ('DM', '디자인경영융합학부'), ('DC', '디자인컨버전스학부'), ('Ani', '영상애니메이션학부'), ('GS', '게임소프트웨어공학전공'), ('GD', '게임그래픽디자인전공'), ('STFm', '과학기술대학자율전공'), ('ArD', '건축디자인과'), ('ArE', '건축공학과'), ('MIE', '기계정보공학과'), ('ShE', '조선해양공학과'), ('BC', '바이오화학공학과'), ('NN', '나노신소재공학과'), ('ECE', '전자전기융합공학과'), ('SCE', '소프트웨어융합공학과'), ('GM', '글로벌경영학과'), ('FI', '금융보험학과'), ('Ac', '회계학과'), ('Ad', '광고홍보학부'), ('IS', '산업스포츠학과'), ('SjFm', '세종캠퍼스자율전공')], default='CS', max_length=5),
        ),
    ]
