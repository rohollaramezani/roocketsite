from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request,'website\index.html')


def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')

def handler404(request,exception):
    return render(request,'errors/404.html',{})

def handler500(request):
    return render(request,'errors/500.html',{})