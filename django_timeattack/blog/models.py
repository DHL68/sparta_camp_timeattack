# restaurant/models.py
from django.db import models


# Create your models here.

class Article(models.Model):
    class Meta:
        db_table = "my_article"

    def __str__(self):
        return self.article_name

    article_name = models.CharField(max_length=100)


class Category(models.Model):
    class Meta:
        db_table = "my_category"

    def __str__(self):
        return self.category_name

    category_name = models.CharField(max_length=100)
    article_category = models.ManyToManyField(Article)