from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='form_auth.html'), name='logout'),
    path('perfil/<int:id>',views.perfil,name='perfil'),
    path('editar/perfil/<int:id>',views.PerfilUpdateView.as_view(),name='editar-perfil'),
    path('favoritar/<int:produto_id>/', views.favoritar_produto, name='favoritar-produto'),
]
