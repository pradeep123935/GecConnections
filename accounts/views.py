from django.shortcuts import render,redirect,HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView,LoginView
from django.urls import reverse_lazy
from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from myblog.models import Post

def Index(request):
	return render(request,'registration/index.html')


class PasswordsChangeView(PasswordChangeView):
	template_name = 'registration/change_password.html'
	success_url= reverse_lazy('home')



class LoginView(LoginView):
	form_class = LoginForm
	template_name='registration/login.html'
	success_url= reverse_lazy('home')


class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')


@login_required
def liked_posts(request):
	liked_post = Post.objects.filter(likes=request.user)
	context = {'liked_post':liked_post}
	return render(request,'registration/liked_posts.html',context)
	

@login_required
def profile(request):
	post = Post.objects.filter(author=request.user)
	coins=post.count()*10
	for i in post:
		coins = coins + i.likes.count()*2
		coins = coins + i.total_comments()*5

	blog_count = post.count()
	context = {'post':post,'blog_count':blog_count,'coins':coins}
	return render(request,'registration/profile.html',context)

@login_required
def updateprofile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
			request.FILES,
			instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request,'registration/update_profile.html',context)

