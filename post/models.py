from django.db import models
from account.models import CustomUser

# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = [ #카테고리 선택지
        ('management', '총무 및 사무'),
        ('business', '영업'),
        ('PerDepart', '인사'),
        ('customerC', '고객상담'),
        ('marketing', '마케팅'),
        ('trade', '유통 및 무역'),
        ('design', '디자인'),
        ('develop', '개발'),
        ('judicial', '법무 및 특허'),
        ('strategy', '전략 및 기획'),
        ('financial', '재무 및 회계'),
        ('sales', '구매 및 조달'),
        ('service', '서비스'),
        ('profession', '전문직'),
        ('medical', '의료 및 제약'),
        ('educ', '교육직'),
        ('construct', '건설 및 인테리어'),
        ('research', '연구 및 생산, 제조'),
        ('media', '미디어'),
        ('etc', '특수'),
    ]
    category = models.CharField(#카테고리
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='develop',
    ) 
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()#올린 날짜
    body = models.TextField()# 내용
    hashtag = models.CharField(max_length=50) #해쉬태그
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)# 이미지
    link = models.CharField(max_length=100, blank=True, null=True)#링크
    
    like = models.ManyToManyField(CustomUser, related_name='likes',blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    def summary(self):
        return self.body[:100]


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content