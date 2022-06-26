from django.db import models

class lotto(models.Model):
    drwNo = models.IntegerField(primary_key=True) # 회차
    drwNoDate = models.DateTimeField(null=True, blank=True) # 날짜
    drwtNo1 = models.IntegerField(null=False) # 1번
    drwtNo2 = models.IntegerField(null=False) # 2번
    drwtNo3 = models.IntegerField(null=False) # 3번
    drwtNo4 = models.IntegerField(null=False) # 4번
    drwtNo5 = models.IntegerField(null=False) # 5번
    drwtNo6 = models.IntegerField(null=False) # 6번
    dnusNo = models.IntegerField(null=False) # 보너스
    firstAccumamnt = models.PositiveBigIntegerField(null=False) # 1등 당첨금

# Create your models here.
