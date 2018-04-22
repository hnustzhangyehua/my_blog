from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.

def home(request, num):
    return HttpResponse("Hello world {}".format(num))

def my_blog(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    #print(post_list)
    return render(request, 'home.html', {'post_list' : post_list})
