from django.db import models
from datetime import datetime

# Create your models here.
#식당 정보가 저장될 모델(DB) 만들어주기!
class Restaurant(models.Model):
    name=models.CharField(max_length=15)
    location=models.CharField(max_length=50,default='')
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)
    #식당에 foodtype 속성 추가.
    CHOICE = (('korean','한식'),('japanese','일식'),
              ('chinese','중식'),('western','양식'),('etc','기타'))
    foodtype = models.CharField(max_length=20, choices=CHOICE,default='*')
    #리스트 정렬용 create_date
    create_date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name

class Filter(models.Model): #식당을 각각 한식, 중식, 일식, 양식으로 필터링해줄 모델도 추가로 생성해줍니다.
    korean = models.BooleanField(default='True')
    chinese = models.BooleanField(default='True')
    japanese = models.BooleanField(default='True')
    western = models.BooleanField(default='True')
    etc = models.BooleanField(default='True')

class Comment(models.Model): #댓글 모델, Model은 DB에서 가져오는것
    rst = models.ForeignKey(Restaurant, on_delete=models.CASCADE)#해당하는 게시글의 댓글이란 의미로 Foreign키 속성 부여
    #on_delete, CACADE면! => 같이 지워지라는 것. 게시글이 사라지면 댓글도 사라지도록!!
    #이렇게 Foreign키 지정이 가능한 이유는 migrate하면서 장고에서 자동으로 migrations 아래에 Board와 Comment에 대한 id를 만들고, PK 지정을 해주기 때문.
    content = models.TextField()
    create_date = models.DateTimeField()