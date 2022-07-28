from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Post(models.Model):
	title = models.CharField(max_length=30)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	description = RichTextField(blank=True,null=True)
	image = models.ImageField(upload_to='',blank=True)
	category = models.CharField(max_length=50)
	snippet = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User,related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def total_comments(self):
		return self.comments.count()

	def __str__(self):
		return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    comm_name = models.CharField(max_length=100,blank=True)
    post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name='comments')
    comment  = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def total_comments(self):
    	return self.comment.count()

    def save(self,*args,**kwargs):
    	self.comm_name = slugify("Comment by" + "-" + str(self.user)+str(self.date))
    	super().save(*args,**kwargs)


    def __str__(self):
        return str(self.user)+" "+str(self.post)

    class Meta:
    	ordering = ['-date']


class Reply(models.Model):
	comment_name = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="replies")
	reply_body = models.TextField()
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "reply_to"+str(self.comment_name)


class Contact(models.Model):
     name = models.TextField()
     email= models.EmailField(max_length=100)
     message= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email

