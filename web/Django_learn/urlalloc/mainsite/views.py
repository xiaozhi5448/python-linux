from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def homepage(request):
    return HttpResponse("hello world!")

def article(request, article_id='0'):
    return HttpResponse('article id:{}'.format(article_id))

def company(request):
    return HttpResponse('Company!')