from django.urls import path
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import views as auth_views

from .views import ProfileEditView, RegisterView

app_name = 'auth'

urlpatterns = (
    path(_('login/'), auth_views.LoginView.as_view(template_name="auth/login.html"), name='login'),
    path(_('register/'), RegisterView.as_view(), name='register'),
    path(_('logout/'), auth_views.LogoutView.as_view(), name='logout'),
    path(_('edit-profile/'), ProfileEditView.as_view(), name='edit-profile'),
)
