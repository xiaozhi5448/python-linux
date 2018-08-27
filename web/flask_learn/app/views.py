#!/usr/bin/env python
# coding=utf-8
from app import app
from flask import render_template, redirect, flash, url_for, request
from .forms import LoginForm


@app.route('/')
@app.route('/index/')
def index():
    user = {'nickname':'xiaozhi'}
    posts =[ 
        {
            'author':{
                'nickname':'xiaoming'
            },
            'body':'this is a compose created by xiaoming'
        },
        {
            'author':{'nickname':'xiaohong'},
            'body':'this is a compose created by xiaohong'
        }
    ]
    title = 'title'
    flash('test flash message')
    return render_template("children.html", title=title, user=user, posts=posts)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    

    if form.validate_on_submit():
        flash('you requested openid:\"'+form.openid.data+'\"remember_me='+str(form.remember_me.data))
        #flash('your email:\"'+form.emailAddress.data+'\" remember_me='+str(form.remember_me.data))
        return 'success'
        #return redirect('/index/')
    return render_template("login.html", title="Sign In", form=form, privoders=app.config['OPENID_PROVIDERS'])
    