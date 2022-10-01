from django.db import models
from django.utils import timezone

class Article(models.Model):
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    published_at = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self) -> str:
        return self.title