from email.policy import default
from tabnanny import verbose
from django.db import models
from django.utils import timezone

class Article(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='عنوان')
    body = models.TextField(verbose_name='متن')
    views = models.IntegerField(default=0,verbose_name='بازدیدها')
    show=models.BooleanField(default=1, verbose_name='نمایش')
    created_at = models.DateTimeField(auto_now_add = True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now = True,verbose_name='به روز رسانی')
    published_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural = 'مقالات'
    
    def __str__(self) -> str:
        return self.title