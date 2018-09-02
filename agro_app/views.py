from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
from django.utils import timezone

from .models import *

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from django.core.files.storage import Storage 
from django.core.files.storage import FileSystemStorage
import datetime
import requests

# Create your views here.
def home(request):
	return render(request,'index.html')

def registration(request):
    # registration module
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/') 

    elif request.method == 'POST':
        user_username = request.POST['username']
        user_password = request.POST['password']
        user_email = request.POST['email']
        user_name = request.POST['name']
        #district = request.POST['district']
        #number  = request.POST['number']

        # checking existing email.
        existing_email = User.objects.filter(email=user_email).first()
        if existing_email is not None:
            message = '"' + user_email + '" already exist. Please try with a different email.'

            return render(request, 'logregi/registration.html',
                          {'error_message': message})

        try:
            user = User.objects.create_user(username=user_username, first_name=user_name, email=user_email)
        except IntegrityError as e: #how work here IntegrityError method?

            e.message = '"' + user_username + '" already exist. Please try with a different username.'

            return render(request, 'registration.html',
                          {'error_message': e.message})

        user.set_password(raw_password=user_password)

        user.is_staff = True
        user.is_superuser = False
        user.is_active = True
        user.save()

        return render(request, 'logregi/registration.html',
                      {'success_message': 'Registration is complete! Please login..'})
    else:
        return render(request, 'logregi/registration.html')

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    else:
        #import login method
        from django.contrib.auth import login
        loginStatus = request.user.is_authenticated

        user = None
        #print(loginStatus)

        if request.method == 'POST':

            uemail = request.POST['email']
            pword = request.POST['password']
            LoginRequestUser = User.objects.filter(email=uemail).first()
            user = authenticate(username=LoginRequestUser, password=pword)
            if user is not None:
                if user.is_active:
                    login(request, user) #???????????
                    # return HttpResponseRedirect('/base/begin/')
                    return HttpResponseRedirect('/home/')
                else:
                    return render(request, 'login.html', {'message': "Its not active user"})
            else:
                return render(request, 'logregi/login.html',
                              {'message': "Invalid login or your account is inactive"})

        elif request.method == 'GET': 
            if (loginStatus == True):
                return HttpResponseRedirect('home/')
            else:
                return render(request, 'logregi/login.html', {})
    return render(request, 'logregi/login.html', {'message': "Invalid User name Or Password",'user': user})#read here atlast

def logout(request):
    if request.user.is_authenticated:
        from django.contrib.auth import logout
        logout(request)
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/home/')
#update password....
'''def cpassword(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
        user=request.user

    elif request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        u = User.objects.filter(id=user.id).first()
        if u is not None:
            usser = User.objects.get(username=user.username)
            usser.set_password(new_password)
            usser.save()
    return render(request,'user&_pblm_d/changepass.html')'''

def posts(request,post_id):
    user=request.user
    #print(user)
    allpost  = Posts.objects.all().order_by("-id")
    paginator = Paginator(allpost, 2)
    page = request.GET.get('page',1)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger: # If page is not an integer, deliver first page.
        lists = paginator.page(1)
    except EmptyPage:        # If page is out of range (e.g. 9999), deliver last page of results.
        lists = paginator.page(paginator.num_pages)

    postd   = Posts.objects.get(id=post_id)
    comments = Comments.objects.order_by("-comment_added_date")
    if request.method == 'GET':
        return render(request,'adminsolu/posts.html',{'lists': lists,'postd': postd,'comments': comments,'page':page})
    elif request.method == 'POST':
        comment_text = request.POST['comment']

        post = Posts.objects.filter(id=post_id).first()
        #print(post)
        if post is not None:
            comments = Comments(posts_id=post.id,user_id=user.id,comment_text=comment_text,is_publish=0)
            comments.save()
            return HttpResponseRedirect('/posts/' + post_id + '')
    return render(request,'adminsolu/posts.html',{'allpost': allpost,'postd': postd,'comments': comments})
    
def posts_details(request,post_id):
    user=request.user
    postd   = Posts.objects.get(id=post_id)
    comments = Comments.objects.order_by("-comment_added_date")

    if request.method == 'GET':
        allpost  = Posts.objects.all().order_by("-id")
        paginator = Paginator(allpost, 2)
        page = request.GET.get('page',1)
        try:
            lists = paginator.page(page)
        except PageNotAnInteger: # If page is not an integer, deliver first page.
            lists = paginator.page(1)
        except EmptyPage:        # If page is out of range (e.g. 9999), deliver last page of results.
            lists = paginator.page(paginator.num_pages)

        return render(request,'adminsolu/posts_details.html',{'postd': postd,'comments': comments,'lists': lists})
    elif request.method == 'POST':
        comment_text = request.POST['comment']

        post = Posts.objects.filter(id=post_id).first()
        print(post)
        if post is not None:
            comments = Comments(posts_id=post.id,user_id=user.id,comment_text=comment_text,is_publish=0)
            comments.save()
            return HttpResponseRedirect('/posts_details/' + post_id + '')
    return render(request,'adminsolu/posts_details.html',{'postd': postd,'comments': comments})

def user_problem(request):
    user = request.user
    problem_text = User_problem.objects.order_by("-id")
    paginator = Paginator(problem_text, 7)
    page = request.GET.get('page',1)#Create no. of pages & (Show 1st page with 7 list(Default 1st page))
    try:
        lists = paginator.page(page)
    except PageNotAnInteger: # If page is not an integer, deliver first page.
        lists = paginator.page(1)
    except EmptyPage:        # If page is out of range (e.g. 9999), deliver last page of results.
        lists = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        title        = request.POST['title']
        problem_text = request.POST['problem_text']
        u = User.objects.filter(id=user.id).first()
        if u is not None:
           save_problem_text = User_problem(problem_text=problem_text,title=title,user_id=u.id,is_publish=0)
           save_problem_text.save()
           return HttpResponseRedirect('/user_problem/')

    return render(request,'user&_pblm_d/user_problem.html',{'lists':lists})
    #showing users problem details other user reply....... and user can comment his/her own post
def user_problem_details(request,pid):
    user = request.user
    user_p_reply  = User_p_reply.objects.order_by("-id")
    problem_textd = User_problem.objects.get(id=pid)
    #for get user problem reply....
    if request.method == 'POST':
        ureply = request.POST['ureply']
        u = User.objects.filter(id=user.id).first()
        if u is not None:
           ureply_text = User_p_reply(problem_reply=ureply,user_id=u.id,user_problem_id=problem_textd.id,is_publish=0)
           ureply_text.save()
           return HttpResponseRedirect('/user_problem_details/' + pid + '')

    return render(request,'user&_pblm_d/n_u_pr_details.html',{'problem_textd': problem_textd ,'user_p_reply': user_p_reply})

def new_posts(request):
    user = request.user

    problem_text = User_problem.objects.all().order_by("-comment_added_date")
    paginator    = Paginator(problem_text, 7) # Show 7 list per page
    page = request.GET.get('page',1)#Create no. of pages & (Show 1st page with 7 list(Default 1st page))
    try:
        lists = paginator.page(page)
    except PageNotAnInteger: # If page is not an integer, deliver first page.
        lists = paginator.page(1)
    except EmptyPage:        # If page is out of range (e.g. 9999), deliver last page of results.
        lists = paginator.page(paginator.num_pages)

    return render(request,'new_posts&details/new_posts.html',{'lists': lists})

def new_posts_dnr(request,npd):
    user = request.user
    problem_text = User_problem.objects.get(id=npd)
    user_p_reply  = User_p_reply.objects.order_by("-comment_added_date")

    if request.method == 'POST':
        problem_reply = request.POST['problem_reply']

        uu = User.objects.filter(id=user.id).first()
        if uu is not None:
           ureply_text = User_p_reply(problem_reply=problem_reply,user_id=uu.id,user_problem_id=problem_text.id,is_publish=0)
           ureply_text.save()
           return HttpResponseRedirect('/new_posts_details/' + npd + '')

    return render(request,'new_posts&details/new_posts_details.html',{'problem_text':problem_text,'user_p_reply':user_p_reply})


def news_technology(request,id):
    news_technology = News_technology.objects.all().order_by('-id')
    get_details     = News_technology.objects.get(id=id)
    return render(request,'news_technology.html',{'news_technology': news_technology,'get_details': get_details})


def experience(request,id):
    experience = Experience.objects.all().order_by('-id')
    get        = Experience.objects.get(id=id)
    return render(request,'experience.html',{'experience': experience,'get': get})


def about_contact(request):
    return render(request,'about_contact.html')