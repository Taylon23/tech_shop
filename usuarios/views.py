from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UpdatePerfilForm
from django.views.generic import UpdateView
from . import models


@login_required
def perfil(request, id):
    perfil = get_object_or_404(models.PerfilUsuario, id=id)
    if perfil.usuario != request.user:
        return redirect('perfil', id=request.user.perfilusuario.id)
    return render(request, 'perfil.html', {'perfil': perfil})


class PerfilUpdateView(UpdateView):
    form_class = UpdatePerfilForm
    template_name = 'editar_perfil.html'
    context_object_name = 'perfil'

    def get_object(self, queryset=None):
        perfil = get_object_or_404(models.PerfilUsuario, id=self.kwargs['pk'])
        if perfil.usuario != self.request.user:
            return redirect('perfil', id=self.request.user.perfilusuario.id)
        return perfil

    def get_success_url(self):
        return reverse_lazy('perfil', kwargs={'id': self.request.user.perfilusuario.id})