from django.contrib import admin

# Register your models here.
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','views','published_at')
    date_hierarchy= 'published_at'
    search_fields=('title','body')
    list_filter=('created_at','published_at')
    ordering=['-published_at']
    
    # fields=('title','body','published_at')
    # exclude=('views',)
    
    fieldsets=(
        ("Main Options",{'fields':("title",'body','published_at')}),
        ("Advanced Option",{
            'classes':('collapse',),
            'fields':('views',)
            }),
    )





# admin.site.register(Article,ArticleAdmin)
