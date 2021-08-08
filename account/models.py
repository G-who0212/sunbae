from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to = "profile/", blank=True, null=True)  #사진

    name = models.CharField(max_length=100)  #이름

    MAJOR_IN_SCHOOL_CHOICES = [ #전공 선택지 
        ('CS', '컴퓨터공학과'), 
        ('ME', '기계시스템디자인공학과'), 
        ('NE', '신소재공학과'), 
        ('CHE', '화학공학과'), 
        ('CEE', '건설환경공학과'), 
        ('EE','전자전기공학부'), 
        ('DE', '산업데이터공학과'), 
        ('Law', '법학부'), 
        ('Mus', '뮤지컬전공'), 
        ('PM', '실용음악전공'), 
        ('Ar', '건축학과'), 
        ('IAr', '실내건축학과'), 
        ('CE', '도시공학과'), 
        ('Kor', '국어국문학과'), 
        ('Eng', '영어영문학과'), 
        ('Fra', '불어불문학과'), 
        ('Ger', '독어독문학과'), 
        ('ArtFm', '미술대학자율전공'), 
        ('Art', '예술학과'), 
        ('Sc', '조소과'), 
        ('Pa', '회화과'), 
        ('OPa', '동양화가'), 
        ('En', '판화과'), 
        ('Ed', '교육학과'), 
        ('KEd', '국어교육과'), 
        ('EEd', '영어교육과'), 
        ('MEd', '수학교육과'), 
        ('HEd', '역사교육과'), 
        ('VD', '시각디자인학과'), 
        ('InD', '산업디자인학과'), 
        ('PG', '도예유리과'), 
        ('WF', '목조형가구학과'), 
        ('MD', '금속조형디자인과'), 
        ('FD', '섬유미술패션디자인과'), 
        ('Man', '경영학과'), 
        ('Ec', '경제학과'), 
        ('SFm', '서울캠퍼스자율전공'), 
        ('DM', '디자인경영융합학부'), 
        ('DC', '디자인컨버전스학부'), 
        ('Ani', '영상애니메이션학부'), 
        ('GS', '게임소프트웨어공학전공'), 
        ('GD', '게임그래픽디자인전공'), 
        ('STFm', '과학기술대학자율전공'), 
        ('ArD', '건축디자인과'), 
        ('ArE', '건축공학과'), 
        ('MIE', '기계정보공학과'), 
        ('ShE', '조선해양공학과'), 
        ('BC', '바이오화학공학과'), 
        ('NN', '나노신소재공학과'), 
        ('ECE', '전자전기융합공학과'), 
        ('SCE', '소프트웨어융합공학과'), 
        ('GM', '글로벌경영학과'), 
        ('FI', '금융보험학과'), 
        ('Ac', '회계학과'), 
        ('Ad', '광고홍보학부'), 
        ('IS', '산업스포츠학과'), 
        ('SjFm', '세종캠퍼스자율전공') 
    ]

    major = models.CharField(  #전공
        max_length=5,
        choices=MAJOR_IN_SCHOOL_CHOICES,
        default='CS',
    )

    studentNum = models.CharField(max_length=10)  #학번

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

    #웹사이트
    websiteName = models.CharField(max_length=150, blank=True, null=True) #이름
    websiteURL = models.CharField(max_length=150, blank=True, null=True) #URL

    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")


class Career(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
	company = models.CharField(max_length=50, blank=True, null=True) #회사
	title = models.CharField(max_length=50, blank=True, null=True) #직함
	CAREER_YEAR_START_CHOICES = [ #시작 연도 선택지
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    ]
	careerYearStart = models.CharField( #시작연도
        max_length=10,
        choices=CAREER_YEAR_START_CHOICES,
        default='2021',
        blank=True, 
        null=True
    )
	CAREER_MONTH_START_CHOICES = [ #시작 월 선택지
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
	careerMonthStart = models.CharField( #시작 월
        max_length=3,
        choices=CAREER_MONTH_START_CHOICES,
        default='1',
        blank=True, 
        null=True
    )
	CAREER_YEAR_END_CHOICES = [ #종료년도 선택지
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    ]
	careerYearEnd = models.CharField( #종료년
        max_length=10,
        choices=CAREER_YEAR_END_CHOICES,
        default='2021',
        blank=True, 
        null=True
    )
	CAREER_MONTH_END_CHOICES = [ #종료 월 선택지
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
	careerMonthEnd = models.CharField( #종료 월 선택
        max_length=3,
        choices=CAREER_MONTH_END_CHOICES,
        default='1',
        blank=True, 
        null=True
    )
	careerRoleAchievement = models.CharField(max_length=200, blank=True, null=True) #역할 / 성과



class Univ(models.Model):
	#대학생 활동
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True) 
	universityActivity = models.CharField(max_length=50, blank=True, null=True) #활동명
	universityTitle = models.CharField(max_length=50, blank=True, null=True) #직함
	UNIVERSITY_YEAR_START_CHOICES = [ #시작년도 선택지
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    ]
	university_YearStart = models.CharField( #시작년도
        max_length=10,
        choices=UNIVERSITY_YEAR_START_CHOICES,
        default='2021',
        blank=True, 
        null=True
    )
	UNIVERSITY_MONTH_START_CHOICES = [ #시작월 선택지
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
	university_MonthStart = models.CharField( #시작 월
        max_length=3,
        choices=UNIVERSITY_MONTH_START_CHOICES,
        default='1',
        blank=True, 
        null=True
    )
	UNIVERSITY_YEAR_END_CHOICES = [#종료년도 선택지
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    ]
	university_YearEnd = models.CharField( #종료 년
        max_length=10,
        choices=UNIVERSITY_YEAR_END_CHOICES,
        default='2021',
        blank=True, 
        null=True
    )
	UNIVERSITY_MONTH_END_CHOICES = [ #종료 월 선택지
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
	university_MonthEnd = models.CharField( #종료 월
        max_length=3,
        choices=UNIVERSITY_MONTH_END_CHOICES,
        default='1',
        blank=True, 
        null=True
    )
	university_RoleAchievement = models.CharField(max_length=200, blank=True, null=True) #역할 / 성과