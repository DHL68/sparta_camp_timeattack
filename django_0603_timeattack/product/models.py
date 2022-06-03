from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "menu_category"

    def __str__(self):
        return self.category_title

    category_title = models.CharField(null=True, max_length=100)


class Drink(models.Model):
    class Meta:
        db_table = "menu_drink"

    def __str__(self):
        return self.drink_name

    drink_name = models.CharField(null=True, max_length=100)
    drink_category = models.ManyToManyField(Category)



