from django.urls import path
from .views import (
	HomeView,
	BlogDetailView,
	AddPostView,
	UpdatePostView,
	DeletePostView,
	LikeView,
	search,
	UserProfileView,
	ContactView,
)

urlpatterns = [
    path('home/',HomeView.as_view(),name="home"),
    path('user/<str:username>',UserProfileView.as_view(),name='user_profile'),
    path('blog/<int:pk>',BlogDetailView.as_view(),name='blog-detail'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('blog/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('blog/<int:pk>/delete',DeletePostView.as_view(),name='delete_post'),
    path('like/<int:pk>',LikeView,name="like_post"),
    path('search/',search,name='search'),
    path('report/',ContactView,name='report'),

]
