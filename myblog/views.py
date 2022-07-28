from django.shortcuts import render,get_object_or_404,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from .models import Post,Comment,Contact
from accounts.models import Profile
from datetime import datetime,date
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PostForm,EditForm,CommentForm,ReplyForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect


def LikeView(request,pk):
	post = get_object_or_404(Post,id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('blog-detail',args=[str(pk)]))


class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']

	def get_context_data(self,*args,**kwargs):
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		user = self.request.user
		post = Post.objects.filter(author=user)
		tot=post.count()*10
		for i in post:
			tot = tot + i.likes.count()*2
			tot = tot + i.total_comments()*5
		context["tot"] = tot
		return context


class UserProfileView(ListView):
	model = Post
	template_name = 'user-profile.html'
	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-post_date')

	def get_context_data(self,*args,**kwargs):
		context = super(UserProfileView,self).get_context_data(*args,**kwargs)
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		blogs = Post.objects.filter(author=user)
		blog_count = blogs.count()
		context["user1"]  = user
		context["blog_count"] = blog_count
		return context


class BlogDetailView(DetailView,FormView):
	model = Post
	template_name = 'detail.html'
	form_class = CommentForm
	second_form_class = ReplyForm

	def get_context_data(self,*args,**kwargs):
		context = super(BlogDetailView,self).get_context_data(*args,**kwargs)
		stuff = get_object_or_404(Post, id = self.kwargs['pk'])
		comments = Comment.objects.filter(post=stuff).order_by('date')
		total_likes = stuff.total_likes()
		total_comments = comments.count()
		liked = False
		user = self.request.user
		if 'form' not in context:
			context['form'] = self.form_class()
		if 'form2' not in context:
			context['form2'] = self.second_form_class()
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked =True
		context["total_likes"] = total_likes
		context["total_comments"] = total_comments
		context["liked"]=liked
		return context

	def post(self,request,*args,**kwargs):
		self.object = self.get_object()
		if 'form' in request.POST:
			form_class = self.form_class
			form_name = 'form'
		else:
			form_class = self.second_form_class
			form_name = 'form2'

		form = self.get_form(form_class)

		if form_name == 'form' and form.is_valid():
			print("Comment form is returned")
			return self.form_valid(form)
		elif form_name == 'form2' and form.is_valid():
			print("reply form is returned")
			return self.form2_valid(form)
	
	def get_success_url(self):
		self.object  = self.get_object()
		pk = self.object.id
		return reverse_lazy('blog-detail',kwargs={'pk':pk})

	def form_valid(self,form):
		self.object = self.get_object()
		fm = form.save(commit=False)
		fm.user = self.request.user
		fm.post = self.object.comments.name
		fm.post_id = self.object.id
		fm.save()
		return HttpResponseRedirect(self.get_success_url())

	def form2_valid(self,form):
		self.object = self.get_object()
		fm = form.save(commit=False)
		fm.user = self.request.user
		fm.comment_name_id = self.request.POST.get('comment.id')
		fm.save()
		return HttpResponseRedirect(self.get_success_url())


class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = ['title','author','description','image']
	success_url = reverse_lazy('home')
	
	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title','description','image']
	success_url = reverse_lazy('home')

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')


def search(request):
	query = request.GET['query']
	if len(query) == 0 or len(query)>50:
		post=[]
		user=[]
	else:
		posttitle = Post.objects.filter(title__icontains=query)
		user = Profile.objects.filter(user__username__icontains=query)
		postcategory = Post.objects.filter(category__icontains =query)
		post = posttitle.union(postcategory)
	context = {'user1':user,'post1':post}
	return render(request,'search.html',context)



def ContactView(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        content =request.POST['content']
       	if len(email)<3 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
           contact=Contact(name=name, email=email,message=content)
           contact.save()
           messages.success(request, "Your issue send successfully we will try to resolve it as soon as possible")
    return render(request, 'contact.html')

