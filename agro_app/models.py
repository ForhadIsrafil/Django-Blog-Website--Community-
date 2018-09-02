from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save #???????
from django.core.files.storage import FileSystemStorage
# Create your models here.
class Posts(models.Model):
	t   = models.CharField(max_length=100)
	im  = models.ImageField()
	d   = models.TextField()

#	def __str__(self):
#		return self.t


class User_problem(models.Model):
	user          = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title         = models.CharField(max_length=60)
	problem_text  = models.TextField(max_length=255)
	comment_added_date = models.DateTimeField(default=timezone.now)
	is_publish         = models.BooleanField(default=False)


class Comments(models.Model):
    posts              = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user               = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment_text       = models.TextField(max_length=255)
    comment_added_date = models.DateTimeField(default=timezone.now)
    is_publish         = models.BooleanField(default=False)

class User_p_reply(models.Model):
	user               = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	user_problem       = models.ForeignKey(User_problem, on_delete=models.CASCADE)
	problem_reply      = models.TextField(max_length=255)
	comment_added_date = models.DateTimeField(default=timezone.now)
	is_publish         = models.BooleanField(default=False)


class News_technology(models.Model):
	title       = models.CharField(max_length=60)
	description = models.TextField()
	im          = models.ImageField()

class Experience (models.Model):
	title       = models.CharField(max_length=60)
	description = models.TextField()
	#im          = models.ImageField()