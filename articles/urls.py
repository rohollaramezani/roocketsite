from django.urls import path 
from . import views
app_name='articles'
urlpatterns = [
    path('',views.articles,name='articles'),
    path('<int:article_id>',views.single_page,name='article'),
    path('article/send',views.send,name='article.send'),
    path('<int:article_id>/edit',views.edit,name='article.edit')
]
