# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import  redirect
from django.http import HttpResponse
from django.template.loader import get_template
#from django.template import RequestContext
from mysite import models, forms
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
# Create your views here.


def register(request):
    years = range(1960, 2021)

    template = get_template('register.html')
    try:
        uid = request.GET['user_id']
        upass = request.GET['user_pass']
        ufcolor = request.GET.getlist('fcolor')
    except:
        uid = None
    if uid != None and upass == '123456':
        verified = True
        year = request.GET['byear']
    else:
        verified = False

    html = template.render(locals())
    return HttpResponse(html)
@csrf_exempt
def login(request):
    template = get_template('login.html')
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username=request.POST['user_name']
            useremail=request.POST['user_email']
            message = 'login successfully！'
        else:
            message = 'login failed!'
    else:
        login_form = forms.LoginForm()
    
    html = template.render(locals())
    response = HttpResponse(html)
    try:
        if username:
            response.set_cookie('username', username)
    except:
        pass
    return response

def logout(request):
    response = redirect('/')
    response.delete_cookie('username')
    return response


def post(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    template = get_template('post.html')
    posts = models.Post.objects.all().order_by('-pub_time')[:30]
   
    moods = models.Mood.objects.all()
    message = ''
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        message= 'cookie 可用!\n'
    else:
        message = 'cookie 不可用\n'
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['user_mood']
    except:
        user_id = None
        message = message + '如果要张贴信息，那么每一个字段都要填'

    if user_id !=None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = message + '请记得您的编辑密码'

    html = template.render(locals())
    return HttpResponse(html)

def posting(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    template = get_template('posting.html')
    moods = models.Mood.objects.all()
    message = "如果要张贴消息，每一条内容都要填！"
    html = template.render(locals())

    return HttpResponse(html)

def listing(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    template = get_template('listing.html')
    posts = models.Post.objects.all()
    moods = models.Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)

@csrf_exempt
def contact(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = 'thanks for your email!'
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_message = form.cleaned_data['user_message']
            mail_body = u'''
            name:{}
            city:{}
            message:{}
            email:{}'''.format(user_name, user_city, user_message,user_email)
            send_mail('subject', mail_body, '18392136027@163.com', ['silenceaxx@gmail.com'])
            
            message = 'thanks for your information!'
        else:
            message = 'please check your information!'
    form = forms.ContactForm()
    template = get_template('contact.html')
    
    html = template.render(locals())
    return HttpResponse(html)