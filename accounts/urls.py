from django.urls import path
from .views import UserRegisterView,Index

urlpatterns = [

	path('register/',UserRegisterView.as_view(),name='register'),
	path('',Index,name='index')
	
	
]