from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from .models import Article
from django.core.paginator import Paginator
# Create your views here.


def articles(request):
    articles=Article.objects.order_by('-created_at')
    paginator=Paginator(articles,2)
    page=request.GET.get('page')
    articles=paginator.get_page(page)
    return render(request,'articles/index.html',{
        'title':'Articles',
        'articles':articles,
        'paginator':paginator,
        'mydata': [1,2,3,4],
        'strdata':'iran food',
        'number':24.23654
    })


def single_page(request,article_id):
    # try:
    #     article=Article.objects.get(id=article_id)
    # except Article.DoesNotExist:
    #        raise Http404("Article Dose not found!!")
    article=get_object_or_404(Article, id = article_id)
    return render(request,"articles/single_page.html",{
        'title':article.title,
        'article':article
    })


def send(request):
    return HttpResponse(request.POST.get('title'))
    return render(request,'articles/send.html')