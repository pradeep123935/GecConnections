from django import forms
from .models import Post,Comment,Reply

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','category','description','image','author','snippet')

		widgets ={
			'title' : forms.TextInput(attrs = {'class': 'form-control','placeholder':'Title'}),
			'author' : forms.TextInput(attrs = {'class': 'form-control','value':'','id':'u1','type':'hidden'}),
			'category' : forms.TextInput(attrs = {'class': 'form-control','placeholder':'Category'}),
			'description' : forms.Textarea(attrs = {'class': 'form-control','label':'content'}),
			'snippet' : forms.Textarea(attrs = {'class': 'form-control','rows':3,'cols':5,'placeholder':'Short Description'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','category','description','image','snippet')

		widgets ={
			'title' : forms.TextInput(attrs = {'class': 'form-control','placeholder':'Title'}),
			'author' : forms.Select(attrs = {'class': 'form-control'}),
			'description' : forms.Textarea(attrs = {'class': 'form-control','rows':3,'cols':5}),
			'category' : forms.TextInput(attrs = {'class': 'form-control'}),
			'snippet' : forms.Textarea(attrs = {'class': 'form-control','rows':3,'cols':5}),
		}

class CommentForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':3,'cols':10}),required=True)

	class Meta:
		model = Comment
		fields = ('comment',)

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ('reply_body',)

		widgets = {
			'reply_body':forms.Textarea(attrs={'class':'form-control','rows':2,'cols':10}),
		}


