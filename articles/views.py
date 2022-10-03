from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from django.core.paginator import Paginator
# Create your views here.
from .forms import SendArticleForm

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


# def send(request):
#     if request.method == 'POST':
#         form=SendArticleForm(request.POST)
#         if form.is_valid():
#             Article.objects.create(
#                 title=form.cleaned_data['title'],
#                 body=form.cleaned_data['body'],
#                 published_at=form.cleaned_data['published_at']
#             )
#             return redirect('articles:articles')
#     else:
#         form=SendArticleForm()
        
#     return render(request,'articles/send.html',{'form':form})

# def edit(request,article_id):
#     article = get_object_or_404(Article, id=article_id)
    
#     if request.method=="POST":
#         form=SendArticleForm(request.POST)
#         if form.is_valid():
#             article.title=form.cleaned_data['title']
#             article.body=form.cleaned_data['body']
#             article.published_at= form.cleaned_data['published_at']
#             article.save()
#         return redirect('articles:articles')
#     else:
#         form=SendArticleForm(article.__dict__)
        
#     return render(request,'articles/edit.html',{'form':form,'article':article})

def edit(request,article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method=="POST":
        form=SendArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:articles')
    else:
        form=SendArticleForm(instance=article)
        
    return render(request,'articles/edit.html',{'form':form,'article':article})

def send(request):
    if request.method == 'POST':
        form=SendArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:articles')
    else:
        form=SendArticleForm()
        
    return render(request,'articles/send.html',{'form':form})
