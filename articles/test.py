from .models import Articles
from django.contrib import admin


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
   def make_hide(self,request,queryset):
       queryset.update(show=0)
       
       