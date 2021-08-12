from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to = "profile/", default = "profile/blank_profile_image.png")  #사진

    name = models.CharField(max_length=100)  #이름

    MAJOR_IN_SCHOOL_CHOICES = [ #전공 선택지 
        ('컴퓨터공학과', '컴퓨터공학과'), 
        ('기계시스템디자인공학과', '기계시스템디자인공학과'), 
        ('신소재공학과', '신소재공학과'), 
        ('화학공학과', '화학공학과'), 
        ('건설환경공학과', '건설환경공학과'), 
        ('전자전기공학부','전자전기공학부'), 
        ('산업데이터공학과', '산업데이터공학과'), 
        ('법학부', '법학부'), 
        ('뮤지컬전공', '뮤지컬전공'), 
        ('실용음악전공', '실용음악전공'), 
        ('건축학과', '건축학과'), 
        ('실내건축학과', '실내건축학과'), 
        ('도시공학과', '도시공학과'), 
        ('국어국문학과', '국어국문학과'), 
        ('영어영문학과', '영어영문학과'), 
        ('불어불문학과', '불어불문학과'), 
        ('독어독문학과', '독어독문학과'), 
        ('미술대학자율전공', '미술대학자율전공'), 
        ('예술학과', '예술학과'), 
        ('조소과', '조소과'), 
        ('회화과', '회화과'), 
        ('동양화가', '동양화가'), 
        ('판화과', '판화과'), 
        ('교육학과', '교육학과'), 
        ('국어교육과', '국어교육과'), 
        ('영어교육과', '영어교육과'), 
        ('수학교육과', '수학교육과'), 
        ('역사교육과', '역사교육과'), 
        ('시각디자인학과', '시각디자인학과'), 
        ('산업디자인학과', '산업디자인학과'), 
        ('도예유리과', '도예유리과'), 
        ('목조형가구학과', '목조형가구학과'), 
        ('금속조형디자인과', '금속조형디자인과'), 
        ('섬유미술패션디자인과', '섬유미술패션디자인과'), 
        ('경영학과', '경영학과'), 
        ('경제학과', '경제학과'), 
        ('서울캠퍼스자율전공', '서울캠퍼스자율전공'), 
        ('디자인경영융합학부', '디자인경영융합학부'), 
        ('디자인컨버전스학부', '디자인컨버전스학부'), 
        ('영상애니메이션학부', '영상애니메이션학부'), 
        ('게임소프트웨어공학전공', '게임소프트웨어공학전공'), 
        ('게임그래픽디자인전공', '게임그래픽디자인전공'), 
        ('과학기술대학자율전공', '과학기술대학자율전공'), 
        ('건축디자인과', '건축디자인과'), 
        ('건축공학과', '건축공학과'), 
        ('기계정보공학과', '기계정보공학과'), 
        ('조선해양공학과', '조선해양공학과'), 
        ('바이오화학공학과', '바이오화학공학과'), 
        ('나노신소재공학과', '나노신소재공학과'), 
        ('전자전기융합공학과', '전자전기융합공학과'), 
        ('소프트웨어융합공학과', '소프트웨어융합공학과'), 
        ('글로벌경영학과', '글로벌경영학과'), 
        ('금융보험학과', '금융보험학과'), 
        ('회계학과', '회계학과'), 
        ('광고홍보학부', '광고홍보학부'), 
        ('산업스포츠학과', '산업스포츠학과'), 
        ('세종캠퍼스자율전공', '세종캠퍼스자율전공') 
    ]

    major = models.CharField(  #전공
        max_length=30,
        choices=MAJOR_IN_SCHOOL_CHOICES,
        default='컴퓨터공학과',
    )

    STUDENT_NUM_CHOICES = [
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),

    ]
    studentNum = models.CharField(
        max_length=10,
        choices=STUDENT_NUM_CHOICES,
        default=21
        )  #학번

    CAMPUS_CHOICES = [#캠퍼스 선택지
        ('서울캠퍼스', '서울캠퍼스'),
        ('세종캠퍼스', '세종캠퍼스'),
    ]

    campus = models.CharField(#캠퍼스
        max_length=50,
        choices=CAMPUS_CHOICES,
        default='서울캠퍼스'
    )

    schoolEmail = models.EmailField(max_length=100) #이메일
    email_auth = models.BooleanField(default=False) # 이메일 인증 여부

    #웹사이트
    websiteName = models.CharField(max_length=150, blank=True, null=True) #이름
    websiteURL = models.CharField(max_length=150, blank=True, null=True) #URL

    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings',blank=True)




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
        ('재직중','재직중'),
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
        (' ','재직중')
    ]
	careerMonthEnd = models.CharField( #종료 월 선택
        max_length=3,
        choices=CAREER_MONTH_END_CHOICES,
        default='1',
        blank=True, 
        null=True
    )




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
        ('활동중','활동중'),
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
        (' ','활동중'),
    ]
	university_MonthEnd = models.CharField( #종료 월
        max_length=3,
        choices=UNIVERSITY_MONTH_END_CHOICES,
        default='1',
        blank=True, 
        null=True
    )
	