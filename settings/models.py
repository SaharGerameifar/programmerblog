from django.db import models
import os

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"setting-image/{final_name}"


class SiteSettings(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان سایت')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='متن کپی رایت', null=True, blank=True)
    logo_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر لوگو')
    instagram = models.CharField(max_length=150, verbose_name=' آدرس اینستاگرام', null=True, blank=True)
    linkedin = models.CharField(max_length=150, verbose_name=' آدرس لينكدين', null=True, blank=True)
    github = models.CharField(max_length=150, verbose_name=' آدرس گيت هاب', null=True, blank=True)
    telegram = models.CharField(max_length=150, verbose_name=' آدرس تلگرام', null=True, blank=True)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'

    def __str__(self):
        return self.title





