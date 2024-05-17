from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from datetime import datetime
from allauth.account.signals import user_logged_in


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100,null=True,blank=True)
    data_nascimento = models.DateField()
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)

    def __str__(self):
        return self.usuario.username
    

@receiver(user_logged_in)
def create_user_profile(sender, request, user, **kwargs):
    # Verifica se o usuário fez login usando o Google
    if user.socialaccount_set.filter(provider='google').exists():
        # Verifica se o usuário já tem um perfil
        if not hasattr(user, 'perfilusuario'):
            # Se não tiver, cria um novo perfil
            PerfilUsuario.objects.create(
                usuario=user,
                nome=user.first_name if user.first_name else user.username,
                # Define a data de nascimento como primeiro de janeiro de 2000
                data_nascimento=datetime(2000, 1, 1),
                foto_perfil=None
            )