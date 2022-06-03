from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)  # 한 줄의 필드
    description = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    # category 에 들어가는 건 글도 아니고, 숫자도 아니고, 리스트도 아니고..
    # Category object 가 들어가야만 한다.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)