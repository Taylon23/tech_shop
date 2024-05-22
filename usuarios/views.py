from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
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
    
@login_required(login_url='login')
def favoritar_produto(request, produto_id):
    if request.method == 'POST':
        produto = get_object_or_404(model_produto.ProdutoModel, id=produto_id)
        user = request.user

        # Verifica se o produto já está favoritado pelo usuário
        favorito, created = models.Favorito.objects.get_or_create(usuario=user, produto=produto)

        if not created:
            # Se já estiver favoritado, remove dos favoritos
            favorito.delete()
            return JsonResponse({'status': 'removed'})
        else:
            return JsonResponse({'status': 'added'})

    return JsonResponse({'status': 'error'}, status=400)

