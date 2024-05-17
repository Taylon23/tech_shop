from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name="singup"),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='form_auth.html'), name="logout"),
]
