from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
# Create your views here.


def articles(request):
    articles=Article.objects.order_by('-created_at')[:10]
    return render(request,'articles/index.html',{
        'title':'Articles',
        'articles':articles
    })


def single_page(request,article_id):
    article=Article.objects.get(id=article_id)
    return render(request,"articles/single_page.html",{
        'title':article.title,
        'article':article
    })