from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class LoginForm(AuthenticationForm):
	username = forms.CharField(label='Roll Number', max_length=10)
	password = forms.CharField(label='Password',widget=forms.TextInput(attrs={'type':'password'}))

	class Meta:
		model = User
		fields = ['username','password']


class SignUpForm(UserCreationForm):
	username = forms.CharField(label='Roll Number', max_length=10)
	password1 = forms.CharField(label='Password',widget=forms.TextInput(attrs={'type':'password'}))
	password2 = forms.CharField(label='Confirm Password',widget=forms.TextInput(attrs={'type':'password'}))

	class Meta:
		model = User
		fields = ('username','password1','password2')
		help_texts = {
		'username' : None
		}

class UserUpdateForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter First Name : ', 'class': 'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name :', 'class': 'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email Address : ', 'class': 'form-control'}))

	class Meta:
		model = User
		fields = ['first_name','last_name','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['pic','bio','branch','year_pass_out','facebook_url','instagram_url','linkedin_url','twitter_url']

		widgets = {
			'bio':forms.Textarea(attrs={'class':'form-control','rows':4,'cols':10,'placeholder':'write your bio here..'}),
			'branch':forms.TextInput(attrs={'class':'form-control','placeholder':'Name of your branch :'}),
			'year_pass_out':forms.TextInput(attrs={'class':'form-control','placeholder':'passing out year : '}),
			'facebook_url':forms.TextInput(attrs={'class':'form-control','placeholder':'facebook profile url : '}),
			'instagram_url':forms.TextInput(attrs={'class':'form-control','placeholder':'instagram profile url'}),
			'linkedin_url':forms.TextInput(attrs={'class':'form-control','placeholder':'linked profile url : '}),
			'twitter_url':forms.TextInput(attrs={'class':'form-control','placeholder':'twitter profile url : '}),
		}

