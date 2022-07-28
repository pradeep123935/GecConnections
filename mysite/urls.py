from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views as user_views

admin.site.site_header = "GEC CONNECTIONS ADMIN PAGE"
admin.site.index_title = "ADMIN PAGE"
admin.site.site_title = "GEC CONNECTIONS"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myblog.urls')),
    path('direct/',include('direct.urls')),
    path('',include('accounts.urls')),
    path('login/', user_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html'
         ),
         name='passwordreset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('profile',user_views.profile,name ='profile'),
    path('update_profile',user_views.updateprofile,name ='update-profile'),
    path('liked_posts',user_views.liked_posts,name="liked_post"),
    path('change-password',user_views.PasswordsChangeView.as_view(),name ='change-password'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
