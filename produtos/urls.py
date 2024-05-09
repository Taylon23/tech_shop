from django.urls import path
from . import views

urlpatterns = [
    path('detalhe/<int:id>',views.detalhe_produto,name='detalhe-produto')
]