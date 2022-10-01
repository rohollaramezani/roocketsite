from django.shortcuts import render

# Create your views here.


def articles(request):
    return render(request,'articles/index.html')


def single_page(request):
    return render(request,"articles/single_page.html")