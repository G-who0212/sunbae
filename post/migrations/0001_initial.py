# Generated by Django 3.2.3 on 2021-08-10 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('management', '총무 및 사무'), ('business', '영업'), ('PerDepart', '인사'), ('customerC', '고객상담'), ('marketing', '마케팅'), ('trade', '유통 및 무역'), ('design', '디자인'), ('develop', '개발'), ('judicial', '법무 및 특허'), ('strategy', '전략 및 기획'), ('financial', '재무 및 회계'), ('sales', '구매 및 조달'), ('service', '서비스'), ('profession', '전문직'), ('medical', '의료 및 제약'), ('educ', '교육직'), ('construct', '건설 및 인테리어'), ('research', '연구 및 생산, 제조'), ('media', '미디어'), ('etc', '특수')], default='develop', max_length=50)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('hashtag', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('like', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
