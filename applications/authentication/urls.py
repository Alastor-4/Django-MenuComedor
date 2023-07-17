from django.urls import path

from . import views

app_name = "auth_app"

# conjunto de urls de login y registro
urlpatterns = [
    path('auth/login/', views.LoginUserView.as_view(), name='auth-login'),
    path('auth/logout/', views.LogoutView.as_view(), name='auth-logout'),
    path('auth/register/', views.UserRegisterView.as_view(), name='auth-register'),
    path('auth/user-verification/<id_user>/', views.CodeVerificationView.as_view(), name='auth-verification'),
]