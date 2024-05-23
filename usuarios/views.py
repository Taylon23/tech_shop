from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .forms import UpdatePerfilForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from . import models
from django.http import JsonResponse
from produtos import models as model_produto


@login_required
def perfil(request, id):
    perfil = get_object_or_404(models.PerfilUsuario, id=id)
    if perfil.usuario != request.user:
        return redirect('perfil', id=request.user.perfilusuario.id)
    return render(request, 'perfil.html', {'perfil': perfil})


class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UpdatePerfilForm
    template_name = 'editar_perfil.html'
    context_object_name = 'perfil'

    def get_object(self, queryset=None):
        perfil = get_object_or_404(
            models.PerfilUsuario, pk=self.kwargs['id'], usuario=self.request.user)
        return perfil

    def get_success_url(self):
        return reverse_lazy('perfil', kwargs={'id': self.request.user.perfilusuario.id})

    def get_initial(self):
        initial = super().get_initial()
        perfil = self.get_object()
        initial['data_nascimento'] = perfil.data_nascimento
        return initial


def favoritar_produto(request, produto_id):
    produto = get_object_or_404(model_produto.ProdutoModel, pk=produto_id)

    if request.user.is_authenticated:
        favorito, created = models.Favorito.objects.get_or_create(
            usuario=request.user, produto=produto)
        if not created:
            favorito.delete()
            return JsonResponse({'status': 'removed'})
        else:
            return JsonResponse({'status': 'ok', 'favoritado': True})
    else:
        login_url = reverse('login')  # Obtém a URL de login
        return JsonResponse({'status': 'error', 'message': 'Usuário não autenticado', 'login_url': login_url})


@login_required(login_url='login')
def list_favoritos(request):
    list_favoritar_produto = models.Favorito.objects.filter(usuario=request.user)
     
    return render(request,'list-favoritos.html',{'lista_favoritos':list_favoritar_produto})
