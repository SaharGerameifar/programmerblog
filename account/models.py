from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    is_author = models.BooleanField(default=False, verbose_name="وضعیت نویسنده")
    special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")
    image = models.ImageField(upload_to="images", verbose_name='تصویر شما براي نمايش در سايت', null=True, blank=True)
    job_title = models.CharField(max_length=200, verbose_name='تخصص', null=True, blank=True)
    linkedin = models.CharField(max_length=150, verbose_name=' آدرس لينكدين', null=True, blank=True)
    github = models.CharField(max_length=150, verbose_name=' آدرس گيت هاب', null=True, blank=True)
    instagram = models.CharField(max_length=150, verbose_name=' آدرس اینستاگرام', null=True, blank=True)
    telegram = models.CharField(max_length=150, verbose_name=' آدرس تلگرام', null=True, blank=True)

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = "وضعیت کاربر ویژه"
