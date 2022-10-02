from django.contrib import admin

# Register your models here.
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','views','published_at','show')
    date_hierarchy= 'published_at'
    search_fields=('title','body')
    list_filter=('created_at','published_at')
    ordering=['-published_at']
    actions=['make_hide','make_show']
    # fields=('title','body','published_at')
    # exclude=('views',)
    
    fieldsets=(
        ("موارد اصلی",{'fields':("title",'body','published_at')}),
        ("موارد بیشتر",{
            'classes':('collapse',),
            'fields':('views','show')
            }),
    )

    def make_hide(self,request,queryset):
        row_articles=queryset.update(show=0)
        
        self.give_message(request,row_articles,'مخفی شدند')
    
    make_hide.short_description="مخفی کردن مقالات انتخابی"

    def make_show(self, request, queryset):
        row_articles=queryset.update(show=1)
        self.give_message(request,row_articles,'نمایش داده شدند')
    make_show.short_description= "نمایش دادن مقالات انتخابی"

    def give_message(self,request,row_articles,type):
        if row_articles==1:
            message_bit="1 مقاله "
        else:
            message_bit='%s مقاله ' % row_articles
        self.message_user(request, '%s به صورت موفق %s' % (message_bit , type))

# admin.site.register(Article,ArticleAdmin)
