"""login_signup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from agro_app.views import *
from django.conf.urls.static import static
from django.conf import settings
import django
'''A Django settings file contains all the configuration of your Django installation.
 This document explains how settings work and which settings are available.
 A settings file is just a Python module with module-level variables.'''


urlpatterns = [
    path('admin/', admin.site.urls),

    path('registration/', registration, name="registration_view"),
    path('login/', login, name="login_view"),
    path('logout/', logout, name="logout"),

    path('home/', home, name="home"),

    path('posts/<post_id>/', posts, name="posts"),
    path('posts_details/<post_id>/', posts_details, name="posts_details"),

    path('user_problem/', user_problem, name="user_problem"),
    path('user_problem_details/<pid>/',user_problem_details,name="user_problem_details"),
    #path('password/', cpassword, name="cpassword"),

    path('new_posts/', new_posts, name="new_posts"),
    path('new_posts_details/<npd>/', new_posts_dnr, name="new_posts_dnr"),
    path('media/<path>/', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),

    path('news_technology/<id>/',news_technology, name='news_technology'),
    path('experience/<id>/', experience, name='experience'),
    path('about_contact/', about_contact, name='about_contact'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # "stattic" Helper function to return a URL pattern for serving files in debug mode: