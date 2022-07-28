from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE,related_name="profile")
	pic  = models.ImageField(default='pic.jpg',upload_to = '',blank = True)
	bio = models.TextField(blank = True)
	branch = models.CharField(max_length=50,blank=True,null=True)
	year_pass_out = models.CharField(max_length=4,blank=True,null=True)
	facebook_url = models.CharField(max_length=299,blank=True,null=True)
	instagram_url = models.CharField(max_length=299,blank=True,null=True)
	linkedin_url = models.CharField(max_length=299,blank=True,null=True)
	twitter_url = models.CharField(max_length=299,blank=True,null=True)

	def __str__(self):
		return f'{self.user.username} Profile'
