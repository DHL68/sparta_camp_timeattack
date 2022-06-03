# Generated by Django 4.0.5 on 2022-06-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_category_description_remove_category_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='drink_category',
        ),
        migrations.AddField(
            model_name='drink',
            name='drink_category',
            field=models.ManyToManyField(to='product.category'),
        ),
    ]
