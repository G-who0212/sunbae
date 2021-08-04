from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)#사진

    name = models.CharField(max_length=100) #이름

    MAJOR_IN_SCHOOL_CHOICES = [ #전공 선택지
        ('CS', '컴퓨터공학과'),
        ('ME', '기계공학과'),
        ('CHE', '화학공학과'),
        ('InD', '산업디자인학과'),
        ('Man', '경영학과'),
    ]
    major = models.CharField(#전공
        max_length=5,
        choices=MAJOR_IN_SCHOOL_CHOICES,
        default='CS',
    )

    studentNum = models.CharField(max_length=10)#학번

    CAMPUS_CHOICES = [#캠퍼스 선택지
        ('SC', '서울캠퍼스'),
        ('SJC', '세종캠퍼스'),
        ('DHN', '대학로캠퍼스'),
    ]
    campus = models.CharField(#캠퍼스
        max_length=50,
        choices=CAMPUS_CHOICES,
        default='SC'
        )

    schoolEmail = models.CharField(max_length=50) #이메일
    #경력
    career1Company = models.CharField(max_length=50, blank=True, null=True) #회사
    career1Title = models.CharField(max_length=50, blank=True, null=True) #직함
    CAREER1YEAR_START_CHOICES = [ #시작 연도 선택지
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    ]
    career1YearStart = models.CharField( #시작연도
        max_length=10,
        choices=CAREER1YEAR_START_CHOICES,
        default='2021',
        blank=True, 
        null=True
    )
    CAREER1MONTH_START_CHOICES = [ #시작 월 선택지
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]
    career1MonthStart = models.CharField( #시작 월
        max_length=3,
        choices=CAREER1MONTH_START_CHOICES,
        default='1',
        blank=True, 
        null=True
    )
    CAREER1YEAR_END_CHOICES = [ #종료년도 선택지
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    ]
    career1YearEnd = models.CharField( #종료년
        max_length=10,
        choices=CAREER1YEAR_END_CHOICES,
        default='2021',
        blank=True, 
        null=True
    )
    CAREER1MONTH_END_CHOICES = [ #종료 월 선택지
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]
    career1MonthEnd = models.CharField( #종료 월 선택
        max_length=3,
        choices=CAREER1MONTH_END_CHOICES,
        default='1',
        blank=True, 
        null=True
    )
    career1RoleAchievement = models.CharField(max_length=200, blank=True, null=True) #역할 / 성과

#대학생 활동
    university1Activity = models.CharField(max_length=50, blank=True, null=True) #활동명
    university1Title = models.CharField(max_length=50, blank=True, null=True) #직함
    UNIVERSITY1YEAR_START_CHOICES = [ #시작년도 선택지
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    ]
    university1YearStart = models.CharField( #시작년도
        max_length=10,
        choices=UNIVERSITY1YEAR_START_CHOICES,
        default='2021',
        blank=True, 
        null=True
    )
    UNIVERSITY1MONTH_START_CHOICES = [ #시작월 선택지
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]
    university1MonthStart = models.CharField( #시작 월
        max_length=3,
        choices=UNIVERSITY1MONTH_START_CHOICES,
        default='1',
        blank=True, 
        null=True
    )
    UNIVERSITY1YEAR_END_CHOICES = [#종료년도 선택지
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    ]
    university1YearEnd = models.CharField( #종료 년
        max_length=10,
        choices=UNIVERSITY1YEAR_END_CHOICES,
        default='2021',
        blank=True, 
        null=True
    )
    UNIVERSITY1MONTH_END_CHOICES = [ #종료 월 선택지
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]
    university1MonthEnd = models.CharField( #종료 월
        max_length=3,
        choices=UNIVERSITY1MONTH_END_CHOICES,
        default='1',
        blank=True, 
        null=True
    )
    university1RoleAchievement = models.CharField(max_length=200, blank=True, null=True) #역할 / 성과

    #웹사이트
    websiteName = models.CharField(max_length=150, blank=True, null=True) #이름
    websiteURL = models.CharField(max_length=150, blank=True, null=True) #URL

