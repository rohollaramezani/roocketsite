from django.urls import path 
from . import views
urlpatterns = [
    path('',views.articles),
    path('singlepage/',views.single_page),
]
