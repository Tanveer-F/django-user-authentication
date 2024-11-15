from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home, name='home'),
    path('accounts/profile/', accounts_views.profile, name='profile'),
    path('accounts/register/', accounts_views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/passwordresetcomplete.html'), name='password_reset_complete'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/passwordchangedone.html'),name='password_change_done'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/passwordresetdone.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/passwordresetconfirm.html'),name='password_reset_confirm'),
   
]
# This code for media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
