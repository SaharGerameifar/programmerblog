# Generated by Django 3.2.9 on 2020-11-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='article.Category', verbose_name='دسته بندی'),
        ),
    ]
