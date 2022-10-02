from django.urls import path 
from . import views
app_name='articles'
urlpatterns = [
    path('',views.articles,name='articles'),
    path('<int:article_id>',views.single_page,name='article'),
]
