from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'webprojectapp/home.html')


def service(request):
    return render(request,'webprojectapp/service.html')


def shop(request):
    return render(request,'webprojectapp/shop.html')


def blog(request):
    return render(request,'webprojectapp/blog.html')


def contact(request):
    return render(request,'webprojectapp/contact.html')